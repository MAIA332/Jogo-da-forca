import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock
from typing import Generator, Dict, Any, Optional
from auth import AuthService, SessionManager
import secrets
import hashlib

class TestUser:
    def __init__(self, username: str, password: str, is_admin: bool = False, session_token: str = None):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.session_token = session_token

    def __repr__(self):
        return f"TestUser({self.username}, admin={self.is_admin})"

def temp_dir(tmp_path: Path) -> Path:
    return tmp_path

def mock_session_manager(monkeypatch: pytest.MonkeyPatch) -> Generator:
    monkeypatch.setattr(SessionManager, 'get_session', MagicMock(return_value=None))
    monkeypatch.setattr(SessionManager, 'create_session', MagicMock(return_value='mock_token'))
    monkeypatch.setattr(SessionManager, 'validate_session', MagicMock(return_value=True))
    monkeypatch.setattr(SessionManager, 'invalidate_session', MagicMock())
    yield
    monkeypatch.undo()

def create_session(user: TestUser) -> str:
    return user.session_token

def test_login_valid_credentials(auth_service: AuthService, tmp_path: Path):
    user = TestUser('testuser', 'securepass123', is_admin=False)
    token = auth_service.login(user)
    assert token is not None
    assert len(token) > 0

def test_login_invalid_credentials(auth_service: AuthService, tmp_path: Path):
    user = TestUser('wronguser', 'wrongpass')
    token = auth_service.login(user)
    assert token is None

def test_register_new_user(auth_service: AuthService, tmp_path: Path):
    user = TestUser('newuser', 'newpass123', is_admin=False)
    result = auth_service.register(user)
    assert result is True

def test_register_duplicate_user(auth_service: AuthService, tmp_path: Path):
    user1 = TestUser('existinguser', 'pass123', is_admin=False)
    auth_service.register(user1)
    user2 = TestUser('existinguser', 'newpass', is_admin=False)
    result = auth_service.register(user2)
    assert result is False

def test_admin_permission(auth_service: AuthService, tmp_path: Path):
    admin_user = TestUser('admin', 'adminpass', is_admin=True)
    auth_service.register(admin_user)
    token = auth_service.login(admin_user)
    assert token is not None
    # Simulate checking admin status via session
    with patch.object(SessionManager, 'get_session') as mock_get:
        mock_get.return_value = {'user': admin_user}
        is_admin = auth_service.check_admin(token)
        assert is_admin is True

def test_session_valid(auth_service: AuthService, tmp_path: Path):
    user = TestUser('sessionuser', 'pass123', is_admin=False)
    token = auth_service.login(user)
    assert auth_service.validate_session(token) is True

def test_session_expired(auth_service: AuthService, tmp_path: Path):
    user = TestUser('expireduser', 'pass123', is_admin=False)
    token = auth_service.login(user)
    # Simulate expired token by setting a very old timestamp in the session
    with patch.object(SessionManager, 'get_session') as mock_get:
        mock_get.return_value = {'user': user, 'expires_at': 0}
        assert auth_service.validate_session(token) is False

def test_session_invalidation(auth_service: AuthService, tmp_path: Path):
    user = TestUser('invalidateuser', 'pass123', is_admin=False)
    token = auth_service.login(user)
    auth_service.invalidate_session(token)
    with patch.object(SessionManager, 'get_session') as mock_get:
        mock_get.return_value = {'user': user, 'expires_at': 0}
        assert auth_service.validate_session(token) is False

@pytest.fixture
def auth_service():
    return AuthService()

@pytest.fixture
def tmp_path():
    return Path(tempfile.mkdtemp())
