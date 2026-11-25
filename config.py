import os
import json
from datetime import datetime, timedelta

# Configurações do Banco de Dados (SQLite para simplicidade e portabilidade)
DB_PATH = "data/auth.db"

# Configurações de Sessão
SESSION_KEY = "auth_session"
SESSION_TIMEOUT = 3600  # 1 hora em segundos

# Definição de Permissões
PERMISSIONS = {
    "ADMIN": ["read", "write", "delete", "manage_users", "manage_rooms"],
    "MEMBER": ["read", "write"]
}

# Caminho para o arquivo de usuários (JSON)
USERS_FILE = "data/users.json"

def get_db_path():
    """Garante que o diretório de dados exista."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return DB_PATH

def get_users_file_path():
    """Garante que o diretório de dados exista."""
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    return USERS_FILE

def load_users() -> dict:
    """Carrega os usuários do arquivo JSON."""
    path = get_users_file_path()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return {}
            return data
    except (json.JSONDecodeError, IOError):
        return {}

def save_users(users: dict):
    """Salva os usuários no arquivo JSON com tratamento de exceções."""
    path = get_users_file_path()
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4, ensure_ascii=False)
    except (IOError, OSError) as e:
        raise IOError(f"Erro ao salvar usuários: {e}")

def hash_password(password: str) -> str:
    """Gera um hash simples da senha (para uso demonstrativo)."""
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str, role: str = "MEMBER") -> bool:
    """Registra um novo usuário."""
    if not username or not password:
        return False
    
    users = load_users()
    
    # Verifica se o usuário já existe
    if username in users:
        return False
    
    # Validação de papel
    if role not in PERMISSIONS:
        role = "MEMBER"
    
    users[username] = {
        "password": hash_password(password),
        "role": role,
        "created_at": datetime.now().isoformat()
    }
    
    save_users(users)
    return True

def authenticate_user(username: str, password: str) -> dict:
    """Autentica um usuário e retorna dados da sessão se válido."""
    users = load_users()
    
    if username not in users:
        return None
    
    user = users[username]
    
    # Verifica senha
    if user["password"] != hash_password(password):
        return None
    
    # Cria objeto de sessão
    session_data = {
        "username": username,
        "role": user["role"],
        "permissions": PERMISSIONS[user["role"]],
        "created_at": datetime.now().isoformat(),
        "expires_at": datetime.now().isoformat()
    }
    
    return session_data

def validate_session(session_data: dict) -> bool:
    """Valida se a sessão ainda é válida (não expirou)."""
    if not session_data:
        return False
    
    try:
        expires_at = datetime.fromisoformat(session_data["expires_at"])
        if datetime.now() > expires_at:
            return False
    except ValueError:
        return False
    
    return True
