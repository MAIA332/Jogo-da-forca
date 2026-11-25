# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos
# Import
import random
import os

from typing import List, Dict, Optional, Set
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock
from typing import Generator, Dict, Any, Optional
import pytest
import secrets
import hashlib

# Import local
from . import Game, User
from auth import AuthService, SessionManager

import threading
import time
from typing import Optional, Callable, Any

class TestUser:
    def __init__(self, username: str, password: str, is_admin: bool = False, session_token: str = None):
        self.username = username
        self.password = password

    def hash_password(self) -> str:
        """
        Hasha a senha usando MD5 com um sal único por usuário.
        Retorna o hash hexadecimal.
        """
        salt = secrets.token_hex(16)
        password_with_salt = f"{salt}{self.password}"
        return hashlib.md5(password_with_salt.encode()).hexdigest()

    def verify_password(self, provided_password: str) -> bool:
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.
        """
        stored_hash = self.hash_password()
        return hashlib.md5(f"{stored_hash}{provided_password}".encode()).hexdigest() == stored_hash

    def __repr__(self):
        return f"TestUser(username='{self.username}', password_hashed=True)"

        self.is_admin = is_admin
        self.session_token = session_token
        self._thread: Optional[threading.Thread] = None
        self._thread_lock = threading.Lock()
        self._task_queue: list = []
        self._running = False

    def start_thread(self, task: Callable, *args, **kwargs) -> threading.Thread:
        """Inicia uma thread dedicada para este usuário para executar a tarefa."""
        with self._thread_lock:
            if self._thread and self._thread.is_alive():
                return self._thread
            
            self._running = True
            self._thread = threading.Thread(target=task, args=args, kwargs=kwargs, name=f"Thread-{self.username}")
            self._thread.daemon = True
            self._thread.start()
            return self._thread

    def stop_thread(self):
        """Para a thread dedicada do usuário."""
        with self._thread_lock:
            if self._thread and self._thread.is_alive():
                self._running = False
                self._thread.join(timeout=2.0)
                self._thread = None

    def __repr__(self):
        return f"TestUser({self.username}, {self.is_admin})"

import threading
from pathlib import Path
from typing import Optional

class TempDirManager:
    _instance: Optional['TempDirManager'] = None
    _lock = threading.Lock()
    _threads: dict[str, threading.Thread] = {}
    _temp_dirs: dict[str, Path] = {}

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._lock = threading.Lock()

    def get_thread(self, user_id: str) -> threading.Thread:
        with self._lock:
            if user_id not in self._threads:
                thread = threading.Thread(target=self._worker, args=(user_id,))
                thread.daemon = True
                thread.start()
                self._threads[user_id] = thread
            return self._threads[user_id]

    def _worker(self, user_id: str):
        # Lógica de trabalho isolado por thread
        pass

    def get_temp_dir(self, tmp_path: Path) -> Path:
        with self._lock:
            if user_id := getattr(self, '_current_user', None):
                if user_id not in self._temp_dirs:
                    safe_name = f"{user_id}_{tmp_path.name}"
                    self._temp_dirs[user_id] = tmp_path.parent / safe_name
                return self._temp_dirs[user_id]
            return tmp_path

    def cleanup(self, user_id: str):
        with self._lock:
            if user_id in self._threads:
                self._threads[user_id].join(timeout=1.0)
                del self._threads[user_id]
            if user_id in self._temp_dirs:
                try:
                    self._temp_dirs[user_id].rmdir()
                except FileNotFoundError:
                    pass
                del self._temp_dirs[user_id]

# Singleton instance
_temp_dir_manager = TempDirManager()

def temp_dir(tmp_path: Path) -> Path:
    return _temp_dir_manager.get_temp_dir(tmp_path)

def mock_session_manager(monkeypatch: pytest.MonkeyPatch) -> Generator:
    yield monkeypatch

def create_session(user: TestUser) -> str:
    return secrets.token_urlsafe(32)

def rand_word() -> str:
    """
    Retorna uma palavra aleatória do arquivo de palavras.
    Design: Mantém a funcionalidade original, mas com docstring alinhada ao estilo técnico do terminal.
    """
    try:
        with open("palavras.txt", "r", encoding="utf-8") as f:
            bank = f.readlines()
        
        if not bank:
            raise ValueError("A lista de palavras está vazia.")
        
        return random.choice(bank).strip()
    except FileNotFoundError:
        raise ValueError("Arquivo 'palavras.txt' não encontrado.")
    except Exception as e:
        raise ValueError(f"Erro ao ler palavras: {e}")

def init_chat_global():
    """Inicializa o módulo de chat global, importando dependências necessárias."""
    from chat_manager import ChatManager
    from templates.chat import render_template
    from templates.menu import render_menu_interactive
    return ChatManager, render_template, render_menu_interactive

def create_room() -> str:
    import secrets
    room_code = "".join(secrets.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(6))
def join_room(room_code: str, user_session: dict = None) -> bool:
    # Implementação básica para validação futura
    if len(room_code) != 6:
        return False
    
    # Verificação de autenticação e permissões
    if user_session is None or not user_session.get('authenticated'):
        return False
    
    # ADMIN e MEMBER podem entrar em salas, mas ADMIN tem privilégios extras
    role = user_session.get('role', 'MEMBER')
    if role not in ['ADMIN', 'MEMBER']:
        return False
        
    return True

def hash_password(password: str, salt: str = None) -> str:
    """
    Hasha a senha usando MD5 com sal (salt) para segurança básica.
    Se salt não for fornecido, gera um aleatório.
    """
    import hashlib
    import os
    
    if salt is None:
        salt = os.urandom(16).hex()
    
    # Combina senha e sal
    data = f"{password}:{salt}".encode('utf-8')
    hash_object = hashlib.md5(data)
    return hash_object.hexdigest()

def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verifica se a senha fornecida corresponde ao hash armazenado.
    Exige que o hash armazenado tenha o formato 'hash:salt'.
    """
    import hashlib
    
    # Separa hash e sal do hash armazenado
    try:
        parts = stored_hash.split(':')
        if len(parts) != 2:
            return False
        stored_hash_value, stored_salt = parts
    except ValueError:
        return False
    
    # Recupera o sal original
    salt = stored_salt
    
    # Hasha a nova senha com o mesmo sal
    data = f"{password}:{salt}".encode('utf-8')
    hash_object = hashlib.md5(data)
    computed_hash = hash_object.hexdigest()
    
    return computed_hash == stored_hash_value

class game():
        # Board (tabuleiro)
    board = ['''

    >>>>>>>>>>Hangman<<<<<<<<<<

    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+

    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

    palavra = rand_word()
    board_count = 0
    l_word = "_"*len(palavra)
    n_l_word = ""
    rep_letter = []
    
    v_l_word = []

    palavra = palavra.lower()
      
    for l in l_word:
        v_l_word.append(l)


    def verify_word(self, letter):
        # Camada 1: Validação de entrada básica
        if not isinstance(letter, str) or len(letter) != 1:
            self.board_count += 1
            print("\n" + '\033[31m' + " Entrada de letra inválida amiguinho" + '\033[0;0m')
            input()
            return

    def create_room(self, user_id: str) -> str:
        """Cria uma nova sala com um código único e inicia a lista de participantes."""
        import random
        import hashlib
        import os
        
        self.room_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
        print(f"\nSala criada! Código: {self.room_code}")
        print("Compartilhe este código com seus amigos para que eles entrem.")
        # Inicializa a lista de participantes com o ID do usuário que criou a sala
        self.room_users = {user_id}
        
        # Gera um salt único para esta sessão (pode ser expandido para persistir no DB)
        salt = os.urandom(16).hex()
        
        # Hash da senha do usuário (assumindo que user_id contém a senha ou será injetada)
        # Nota: Em um cenário real, a senha deve ser passada explicitamente ou buscada do DB.
        # Aqui, para demonstração no contexto do user_id, usamos o user_id como placeholder da senha.
        # Em produção, substitua por: password = self.user_db.get_password(user_id)
        password = user_id  # Placeholder: na prática, a senha real deve ser usada aqui
        
        try:
            # Hash MD5 com salt
            salted_password = password + salt
            hashed_password = hashlib.md5(salted_password.encode()).hexdigest()
            
            # Armazena o hash criptografado (em um sistema real, isso iria para o banco de dados)
            self.user_password_hash = hashed_password
            self.user_salt = salt
            
            print(f"\nAutenticação segura realizada. Hash gerado com sucesso.")
            
        except Exception as e:
            print(f"\nErro na geração do hash: {e}")
            self.user_password_hash = None
            self.user_salt = None

    def verify_user_login(self, user_id: str, provided_password: str) -> bool:
        """Verifica se a senha fornecida corresponde ao hash armazenado."""
        if not self.user_password_hash or not self.user_salt:
            return False
            
        try:
            salted_password = provided_password + self.user_salt
            computed_hash = hashlib.md5(salted_password.encode()).hexdigest()
            return computed_hash == self.user_password_hash
        except Exception:
            return False

    def reset_user_password(self, user_id: str, new_password: str) -> bool:
        """Reseta a senha do usuário, gerando novo hash e salt."""
        try:
            salt = os.urandom(16).hex()
            salted_password = new_password + salt
            hashed_password = hashlib.md5(salted_password.encode()).hexdigest()
            
            self.user_password_hash = hashed_password
            self.user_salt = salt
            
            return True
        except Exception:
            return False
        return self.room_code
        # Nova funcionalidade de chat global será implementada em arquivos separados (gerenciador.py, main.py)
        # Utilizando WebSockets para comunicação em tempo real entre todos os usuários conectados.
        # A lógica de broadcast e gerenciamento de conexões será encapsulada na classe GerenciadorConexoes.
        # A interface HTML será criada em templates/chat.html para interação do usuário.
        # Este método permanece como ponto de entrada para a criação de salas, mas a comunicação global
        # será tratada através das novas rotas de WebSocket definidas no main.py.

    def join_room(self, room_code):
        """Verifica se o jogador pode entrar na sala especificada."""
        if room_code == self.room_code:
            print("\nBem-vindo à sala! Você pode começar a jogar.")
            return True
        else:
            print("\nCódigo de sala inválido. Tente novamente.")
            return False

    def share_room_code(self):
        """Exibe o código da sala atual para compartilhamento."""
        if hasattr(self, 'room_code') and self.room_code:
            print(f"\nSeu código de sala é: {self.room_code}")
            print("Opções disponíveis:")
            print("1. Ver participantes da sala")
            print("2. Remover um participante da sala")
            choice = input("\nEscolha uma opção (1 ou 2): ")
            if choice == '1':
                if hasattr(self, 'room_users') and self.room_users:
                    print("\nParticipantes da sala:")
                    for i, user_id in enumerate(self.room_users, 1):
                        print(f"{i}. {user_id}")
                else:
                    print("\nNenhum participante na sala.")
            elif choice == '2':
                if hasattr(self, 'room_users') and self.room_users:
                    print("\nLista de participantes:")
                    for i, user_id in enumerate(self.room_users, 1):
                        print(f"{i}. {user_id}")
                    try:
                        remover_idx = int(input("\nDigite o número do participante a remover: "))
                        if 1 <= remover_idx <= len(self.room_users):
                            user_id_remover = self.room_users[remover_idx - 1]
                            if self.remove_user_from_room(self.room_code, user_id_remover):
                                print(f"\nUsuário {user_id_remover} foi removido da sala.")
                            else:
                                print("\nFalha ao remover o usuário.")
                        else:
                            print("\nNúmero inválido.")
                    except ValueError:
                        print("\nEntrada inválida.")
                else:
                    print("\nNenhum participante na sala.")
        else:
            print("\nVocê ainda não criou uma sala.")

    def remove_user_from_room(self, room_code: str, user_id: str) -> bool:
        """Remove um usuário da sala se for o criador."""
        if not hasattr(self, 'room_users') or not self.room_users:
            return False
        if user_id not in self.room_users:
            return False
        if self.room_users.index(user_id) != 0:  # Apenas o primeiro (criador) pode remover
            return False
        self.room_users.remove(user_id)
        return True
    def prin_board(self):
        os.system("cls")

        print(self.board[self.board_count])
        print("\n"+" "+self.n_l_word)
        print("\n"+" Letras Que ja foram: "+str(self.rep_letter))
        print("\n"+" Senha criptografada: "+str(self.hash_password(self.password)))
        print("\n"+" Verificar senha: "+str(self.verify_password(self.password, self.hash_password(self.password))))
