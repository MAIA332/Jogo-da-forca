# tests/__init__.py
"""
Pacote de testes para o sistema.
Fornece fixtures isolados e utilitários para testes de autenticação e autorização.
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock
from typing import Generator, Dict, Any, Optional


class TestUser:
    """Fixture para simular usuários com credenciais válidas e inválidas."""
    
    def __init__(self, username: str, password: str, is_admin: bool = False, session_token: str = None):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.session_token = session_token or f"sess_{username}_{id(self)}"
        self.user_id = f"user_{username}"
        self.role = "admin" if is_admin else "user"
        
    def __repr__(self):
        return f"TestUser({self.username}, admin={self.is_admin})"


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Cria um diretório temporário isolado para testes."""
    return tmp_path


@pytest.fixture
def mock_session_manager(monkeypatch: pytest.MonkeyPatch) -> Generator:
    """Simula um gerenciador de sessões com controle de validade."""
    manager = MagicMock()
    
    def create_session(user: TestUser) -> str:
        return user.session_token
    
    def validate_session(token: str) -> Optional[Dict[str, Any]]:
        if token.startswith("sess_expired_"):
            return None
        return {
            "user": user,
            "valid": True,
            "expires_in": 3600
        }
    
    def invalidate_session(token: str):
        pass
    
    monkeypatch.setattr("tests.auth.SessionManager", lambda: manager)
    monkeypatch.setattr(manager, "create_session", create_session)
    monkeypatch.setattr(manager, "validate_session", validate_session)
    monkeypatch.setattr(manager, "invalidate_session", invalidate_session)
    
    yield manager


@pytest.fixture
def mock_auth_service(monkeypatch: pytest.MonkeyPatch) -> Generator:
    """Simula um serviço de autenticação com lógica de verificação."""
    service = MagicMock()
    
    def authenticate(username: str, password: str) -> Optional[TestUser]:
        if username == "admin" and password == "admin123":
            return TestUser("admin", "admin123", is_admin=True)
        elif username == "user" and password == "user123":
            return TestUser("user", "user123", is_admin=False)
        return None
    
    def check_permission(user: TestUser, resource: str) -> bool:
        return user.is_admin if resource == "admin_panel" else True
    
    monkeypatch.setattr("tests.auth.AuthService", lambda: service)
    monkeypatch.setattr(service, "authenticate", authenticate)
    monkeypatch.setattr(service, "check_permission", check_permission)
    
    yield service


@pytest.fixture
def valid_user() -> TestUser:
    """Usuário válido para testes de login."""
    return TestUser("user", "user123")


@pytest.fixture
def admin_user() -> TestUser:
    """Usuário administrador para testes de autorização."""
    return TestUser("admin", "admin123", is_admin=True)


@pytest.fixture
def invalid_credentials() -> tuple:
    """Credenciais inválidas para testes de falha de login."""
    return ("wrong_user", "wrong_pass")


@pytest.fixture
def expired_session_token() -> str:
    """Token de sessão expirado para testes de validação."""
    return "sess_expired_invalid_token"


@pytest.fixture
def valid_session_token() -> str:
    """Token de sessão válido para testes de validação."""
    return "sess_valid_token_123"


@pytest.fixture
def room_code() -> str:
    """Código de sala para testes de gerenciamento de salas."""
    return "room_001"


@pytest.fixture
def user_session(valid_user: TestUser) -> Dict[str, Any]:
    """Dicionário de sessão simulado para testes de rooms."""
    return {
        "user_id": valid_user.user_id,
        "username": valid_user.username,
        "role": valid_user.role,
        "token": valid_user.session_token,
        "active": True
    }


@pytest.fixture
def admin_session(admin_user: TestUser) -> Dict[str, Any]:
    """Dicionário de sessão administrador para testes de rooms."""
    return {
        "user_id": admin_user.user_id,
        "username": admin_user.username,
        "role": admin_user.role,
        "token": admin_user.session_token,
        "active": True
    }


@pytest.fixture
def expired_user_session() -> Dict[str, Any]:
    """Sessão de usuário expirada para testes de rooms."""
    return {
        "user_id": "user_expired",
        "username": "expired_user",
        "role": "user",
        "token": "sess_expired",
        "active": False
    }


@pytest.fixture
def mock_chat_manager(monkeypatch: pytest.MonkeyPatch) -> Generator:
    """Simula um gerenciador de chats."""
    manager = MagicMock()
    monkeypatch.setattr("tests.chat_manager.ChatManager", lambda: manager)
    yield manager


@pytest.fixture
def mock_templates(monkeypatch: pytest.MonkeyPatch) -> Generator:
    """Simula renderização de templates."""
    render_menu = MagicMock(return_value="Menu Rendered")
    render_chat = MagicMock(return_value="Chat Rendered")
    
    monkeypatch.setattr("tests.templates.menu.render_menu_interactive", render_menu)
    monkeypatch.setattr("tests.templates.chat.render_template", render_chat)
    
    yield render_menu, render_chat


@pytest.fixture
def isolated_user_data(temp_dir: Path) -> Path:
    """Cria um diretório isolado para dados de usuário temporários."""
    user_data_dir = temp_dir / "user_data"
    user_data_dir.mkdir(exist_ok=True)
    yield user_data_dir
    # Limpeza automática após o teste
    shutil.rmtree(user_data_dir, ignore_errors=True)


@pytest.fixture
def monkeypatch_session(monkeypatch: pytest.MonkeyPatch) -> Generator:
    """Fixture para patchear sessões específicas."""
    yield monkeypatch
    # Garante que os patches sejam limpos
    monkeypatch.undo()
