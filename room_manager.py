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

    def create_room(self, user_id: str) -> str:
        """Cria uma nova sala e retorna seu código."""
        room_code = f"room_{random.randint(1000, 9999)}"
        self.rooms[room_code] = {
            "users": [],
            "creator": user_id
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

    def get_room_users(self, room_code: str) -> List[str]:
        """Retorna a lista de usuários em uma sala."""
        if room_code not in self.users_in_rooms:
            return []
        return list(self.users_in_rooms[room_code])

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
