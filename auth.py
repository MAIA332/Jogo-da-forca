import os
import json
import hashlib
import secrets
from datetime import datetime, timedelta

def get_db_path():
    return os.path.join(os.path.dirname(__file__), "data", "app.db")

def get_users_file_path():
    return os.path.join(os.path.dirname(__file__), "data", "users.json")

def load_users() -> dict:
    """Carrega os usuários do arquivo JSON. Retorna um dicionário vazio se não existir."""
    try:
        with open(get_users_file_path(), "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return {}
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    except Exception:
        return {}

def save_users(users: dict):
    """Salva os usuários no arquivo JSON."""
    try:
        os.makedirs(os.path.dirname(get_users_file_path()), exist_ok=True)
        with open(get_users_file_path(), "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)
    except IOError:
        raise

def hash_password(password: str) -> str:
    """Hasha a senha usando SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(username: str, password: str, role: str = "MEMBER") -> bool:
    """Registra um novo usuário. Retorna True se sucesso, False se falha."""
    users = load_users()
    
    # Validações básicas
    if not username or not password:
        return False
    
    if username in users:
        return False
    
    # Validação de permissão (apenas ADMIN pode criar ADMIN)
    if role == "ADMIN" and username != "admin":
        return False
    
    # Hash da senha
    hashed_password = hash_password(password)
    
    users[username] = {
        "password": hashed_password,
        "role": role,
        "created_at": datetime.now().isoformat()
    }
    
    save_users(users)
    return True

def authenticate_user(username: str, password: str) -> dict:
    """Autentica um usuário. Retorna um dicionário com dados da sessão ou None."""
    users = load_users()
    
    if username not in users:
        return None
    
    user_data = users[username]
    
    # Verifica senha
    if user_data["password"] != hash_password(password):
        return None
    
    # Cria token de sessão
    session_token = secrets.token_urlsafe(32)
    session_expires = datetime.now() + timedelta(hours=24)
    
    return {
        "username": username,
        "role": user_data["role"],
        "token": session_token,
        "expires": session_expires.isoformat()
    }

def validate_session(session_data: dict) -> bool:
    """Valida se a sessão ainda é válida."""
    if not session_data or "expires" not in session_data:
        return False
    
    try:
        expires_str = session_data["expires"]
        expires = datetime.fromisoformat(expires_str)
        return datetime.now() < expires
    except (ValueError, TypeError):
        return False
