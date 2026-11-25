# room_manager.py

import random
import os
from typing import List, Dict, Optional, Set
from classes import Game, User

class RoomManager:
    def __init__(self):
        import threading
        import queue
        from datetime import datetime

        self.rooms: Dict[str, Dict] = {}
        self.users_in_rooms: Dict[str, Set[str]] = {}  # room_code -> set of user_ids
        self.room_creators: Dict[str, str] = {}  # room_code -> user_id
        self.chat_history: List[Dict] = []  # Lista para armazenar mensagens de chat
        self.current_chat_room: str = None  # Código da sala atual para o chat
        self._thread_pool: Dict[str, threading.Thread] = {}  # Mapeamento de usuário -> thread
        self._user_queues: Dict[str, queue.Queue] = {}  # Filas de mensagens por usuário
        self._lock = threading.Lock()  # Proteção para operações críticas

    def _get_or_create_user_thread(self, user_id: str) -> threading.Thread:
        """Garante que uma thread dedicada exista para o usuário."""
        if user_id not in self._thread_pool:
            queue = queue.Queue()
            self._user_queues[user_id] = queue
            thread = threading.Thread(target=self._user_message_handler, args=(user_id, queue), daemon=True)
            thread.start()
            self._thread_pool[user_id] = thread
        return self._thread_pool[user_id]

    def _user_message_handler(self, user_id: str, queue: queue.Queue):
        """Gerencia mensagens recebidas pela thread do usuário."""
        while True:
            try:
                msg = queue.get_nowait()
                if msg is None:  # Sinal de parada
                    break
                self._process_message(user_id, msg)
            except queue.Empty:
                continue

    def _process_message(self, user_id: str, message_data: Dict):
        """Processa a mensagem dentro da thread do usuário."""
        room_code = message_data.get('room')
        if room_code:
            if room_code not in self.rooms:
                self.rooms[room_code] = {'users': set(), 'messages': []}
            if user_id not in self.rooms[room_code]['users']:
                self.rooms[room_code]['users'].add(user_id)
            self.rooms[room_code]['messages'].append(message_data)
            self.users_in_rooms[room_code] = self.rooms[room_code]['users']
            self._broadcast_to_room(room_code, message_data)
        else:
            self.chat_history.append(message_data)

    def _broadcast_to_room(self, room_code: str, message: Dict):
        """Envia a mensagem para todos os usuários na sala (exceto o remetente)."""
        if room_code not in self.users_in_rooms:
            return
        for user_id in self.users_in_rooms[room_code]:
            if user_id != message.get('sender'):
                self._send_to_user(user_id, message)

    def _send_to_user(self, user_id: str, message: Dict):
        """Envia mensagem para a fila de um usuário específico."""
        if user_id in self._user_queues:
            self._user_queues[user_id].put(message)
        self.chat_messages: Dict[str, List[str]] = {}  # room_code -> lista de mensagens
        self.chat_colors = {
            'user': '\033[92m',  # Verde
            'system': '\033[94m',  # Azul
            'error': '\033[91m',  # Vermelho
            'reset': '\033[0m'
        }
        self._thread_pool: Dict[int, threading.Thread] = {}  # Mapeamento de thread por ID de cliente
        self._client_lock = threading.Lock()  # Proteção para operações de thread/cliente
        self._active_clients: Set[int] = set()  # Conjunto de IDs de clientes ativos
        self._client_data_lock = threading.Lock()  # Lock para garantir consistência de dados entre threads

    def create_room(self, user_id: str, username: str = None, role: str = None) -> str:
        """Cria uma nova sala e retorna seu código.
        
        Args:
            user_id: ID único do usuário.
            username: Nome de usuário (opcional, usado para logs ou display).
            role: Permissão do usuário (ADMIN ou MEMBER).
        """
        # Validação de permissão: apenas usuários com role ADMIN podem criar salas
        if role not in ["ADMIN", "MEMBER"]:
            raise ValueError("Apenas usuários com role ADMIN ou MEMBER podem criar salas.")
        
        room_code = f"room_{random.randint(1000, 9999)}"
        self.rooms[room_code] = {
            "users": [],
            "creator": user_id,
            "creator_username": username,
            "creator_role": role,
            "status": "active",
            "color": "#00ff41"  # Verde estilo terminal
        }
        self.users_in_rooms[room_code] = {user_id}
        self.room_creators[room_code] = user_id
        return room_code

    def join_room(self, room_code: str, user_id: str) -> bool:
        """Tenta fazer um usuário entrar em uma sala."""
        if room_code not in self.rooms:
            return False
        
        if user_id in self.users_in_rooms[room_code]:
            return True  # Já está na sala
        
        self.rooms[room_code]["users"].append(user_id)
        self.users_in_rooms[room_code].add(user_id)
        return True

    def leave_room(self, room_code: str, user_id: str) -> bool:
        """Tenta fazer um usuário sair de uma sala."""
        if room_code not in self.users_in_rooms[room_code]:
            return False
        
        self.users_in_rooms[room_code].discard(user_id)
        if self.users_in_rooms[room_code] == {user_id}:
            del self.users_in_rooms[room_code]
        return True

    def get_room_users(self, room_code: str, current_user: Optional[Dict[str, Any]] = None) -> List[str]:
        """Retorna a lista de usuários em uma sala, filtrando por permissão se necessário.
        
        Args:
            room_code: Código da sala.
            current_user: Dicionário contendo 'username' e 'is_admin' do usuário logado (opcional).
            
        Returns:
            Lista de usernames na sala.
        """
        if room_code not in self.users_in_rooms:
            return []
        
        users = list(self.users_in_rooms[room_code])
        
        # Se o usuário atual não tiver permissão de ADMIN, filtra os usuários retornados
        # para exibir apenas membros, a menos que o próprio usuário seja ADMIN.
        if current_user is not None:
            is_current_admin = current_user.get('is_admin', False)
            current_username = current_user.get('username', '')
            
            if not is_current_admin and current_username in users:
                users.remove(current_username)
        
        return users

    def _handle_client_thread(self, client_socket, client_data: Dict[str, Any]):
        """Gerencia a conexão de um cliente em uma thread dedicada.
        
        Isola o processamento de cada cliente logado em uma thread própria,
        garantindo eficiência e consistência de dados ao evitar bloqueios
        na thread principal do servidor.
        
        Args:
            client_socket: Socket de conexão do cliente.
            client_data: Dados do cliente (username, session_id, etc.).
        """
        try:
            username = client_data.get('username', 'anonymous')
            session_id = client_data.get('session_id', 'unknown')
            
            # Registrar a entrada do usuário na sala atual
            if 'room_code' in client_data:
                room_code = client_data['room_code']
                if room_code not in self.users_in_rooms:
                    self.users_in_rooms[room_code] = set()
                self.users_in_rooms[room_code].add(username)
            
            # Processar mensagens do cliente em loop
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    
                    message = data.decode('utf-8').strip()
                    if message:
                        # Simulação de processamento de mensagem
                        # Em implementação real, aqui entraria a lógica de broadcast
                        # ou envio de resposta específica para este thread
                        pass
                        
                except Exception as e:
                    break
                    
        except Exception as e:
            # Log de erro da thread (opcional, sem bloquear o sistema)
            pass
        finally:
            # Limpar a saída do usuário da sala atual
            if 'room_code' in client_data:
                room_code = client_data['room_code']
                if room_code in self.users_in_rooms:
                    self.users_in_rooms[room_code].discard(username)
            
            # Encerrar a conexão
            client_socket.close()

    def remove_user_from_room(self, room_code: str, user_id: str) -> bool:
        """
        Remove um usuário de uma sala.
        Apenas o criador da sala pode remover outros usuários.
        """
        if room_code not in self.rooms:
            return False
        
        current_creator = self.room_creators.get(room_code)
        if current_creator != user_id:
            return False  # Apenas o criador pode remover
        
        if room_code not in self.users_in_rooms:
            return False
        
        if user_id not in self.users_in_rooms[room_code]:
            return False  # Usuário não está na sala
        
        self.users_in_rooms[room_code].discard(user_id)
        if self.users_in_rooms[room_code] == {user_id}:
            del self.users_in_rooms[room_code]
        return True

    def get_room_info(self, room_code: str) -> Optional[Dict]:
        """Retorna informações da sala (usuários e criador)."""
        if room_code not in self.rooms:
            return None
        return {
            "users": list(self.users_in_rooms.get(room_code, [])),
            "creator": self.room_creators.get(room_code)
        }

# Exemplo de uso
if __name__ == "__main__":
    manager = RoomManager()
    
    # Criar sala
    room_code = manager.create_room("user_1")
    print(f"Sala criada: {room_code}")
    
    # Entrar na sala
    manager.join_room(room_code, "user_1")
    manager.join_room(room_code, "user_2")
    
    # Verificar usuários
    users = manager.get_room_users(room_code)
    print(f"Usuários na sala: {users}")
    
    # Criador remove um usuário
    manager.remove_user_from_room(room_code, "user_1")
    users = manager.get_room_users(room_code)
    print(f"Usuários após remoção: {users}")
    
    # Tentar remover sem ser o criador (deveria falhar)
    manager.remove_user_from_room(room_code, "user_2")  # user_2 não é o criador
    users = manager.get_room_users(room_code)
    print(f"Usuários após tentativa falha: {users}")
