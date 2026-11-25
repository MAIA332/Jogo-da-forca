# room_manager.py

import random
import os
from typing import List, Dict, Optional, Set
from classes import Game, User

class RoomManager:
    def __init__(self):
        self.rooms: Dict[str, Dict] = {}
        self.users_in_rooms: Dict[str, Set[str]] = {}  # room_code -> set of user_ids
        self.room_creators: Dict[str, str] = {}  # room_code -> user_id
        self.chat_history: List[Dict] = []  # Lista para armazenar mensagens de chat
        self.current_chat_room: str = None  # Código da sala atual para o chat
        self.chat_messages: Dict[str, List[str]] = {}  # room_code -> lista de mensagens
        self.chat_colors = {
            'user': '\033[92m',  # Verde
            'system': '\033[94m',  # Azul
            'error': '\033[91m',  # Vermelho
            'reset': '\033[0m'
        }

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
