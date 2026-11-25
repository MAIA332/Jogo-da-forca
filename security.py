import hashlib
import os
from typing import Optional

class PasswordHasher:
    """Gerenciador de hashing de senhas com MD5 e sal."""
    
    @staticmethod
    def hash_password(password: str, salt: Optional[str] = None) -> str:
        """
        Hasha uma senha usando MD5 com um sal opcional.
        
        Args:
            password: A senha a ser hashada.
            salt: Sal opcional para aumentar a segurança. Se None, gera um aleatório.
            
        Returns:
            String hashado da senha.
        """
        if salt is None:
            salt = os.urandom(16).hex()
        
        combined = f"{salt}{password}"
        return hashlib.md5(combined.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, stored_hash: str) -> bool:
        """
        Verifica se uma senha corresponde ao hash armazenado.
        
        Args:
            password: A senha fornecida pelo usuário.
            stored_hash: O hash armazenado no banco de dados.
            
        Returns:
            True se a senha estiver correta, False caso contrário.
        """
        # Extrai o sal do hash armazenado (formato: <sal><hash>)
        # Assumindo que o hash armazenado segue o padrão gerado por hash_password
        if len(stored_hash) < 32:
            return False
            
        # O sal é 32 caracteres (16 bytes hex), o hash é 32 caracteres
        salt = stored_hash[:32]
        stored_hash_only = stored_hash[32:]
        
        generated_hash = PasswordHasher.hash_password(password, salt)
        return generated_hash == stored_hash_only
