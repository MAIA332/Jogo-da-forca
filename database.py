import os
import json
import hashlib
from datetime import datetime, timedelta

def get_db_path():
    return os.path.join(os.path.dirname(__file__), "users.json")

def get_users_file_path():
    return get_db_path()

def load_users() -> dict:
    path = get_users_file_path()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_users(users: dict):
    path = get_users_file_path()
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(username: str, password: str, role: str = "MEMBER") -> bool:
    users = load_users()
    if username in users:
        return False
    users[username] = {
        "password": hash_password(password),
        "role": role,
        "created_at": datetime.now().isoformat()
    }
    save_users(users)
    return True

def authenticate_user(username: str, password: str) -> dict:
    users = load_users()
    if username not in users:
        return None
    user = users[username]
    if user["password"] != hash_password(password):
        return None
    return {
        "username": username,
        "role": user["role"],
        "token": generate_session_token(username)
    }

def validate_session(session_data: dict) -> bool:
    if not session_data or "token" not in session_data:
        return False
    # Implementação simplificada de validação de token
    # Em produção, usar JWT ou verificar contra um banco de dados de sessões
    return True

def generate_session_token(username: str) -> str:
    import secrets
    return secrets.token_urlsafe(32)
