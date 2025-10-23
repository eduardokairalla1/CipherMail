"""
Service for encrypting and decrypting messages.
"""

# --- IMPORTS ---
from cryptography.fernet import Fernet

import base64
import hashlib


# --- TYPES ---
from typing import Optional


# --- CODE ---
class EncryptionManager:
    """
    Handles message encryption and decryption
    """

    @staticmethod
    def normalize_key(key: str) -> bytes:
        """
        Normalizes user key to valid Fernet key format
        Uses SHA256 to create a 32-byte key

        :param key: User-provided key

        :return: Normalized key in bytes
        """
        hash_object = hashlib.sha256(key.encode())
        return base64.urlsafe_b64encode(hash_object.digest())


    @staticmethod
    def encrypt(message: str, key: str) -> str:
        """
        Encrypts a message using the provided key
        
        :param message: Message to encrypt
        :param key: Key to use for encryption

        :return: Encrypted message as a string
        """
        # Normalize the key
        normalized_key = EncryptionManager.normalize_key(key)

        # Create Fernet instance
        fernet = Fernet(normalized_key)

        # Encrypt the message
        encrypted = fernet.encrypt(message.encode())

        # Return encrypted message as string
        return encrypted.decode()


    @staticmethod
    def decrypt(encrypted_message: str, key: str) -> Optional[str]:
        """
        Decrypts a message using the provided key

        :param encrypted_message: Encrypted message to decrypt
        :param key: Key to use for decryption

        :return: Decrypted message as a string, or None if decryption fails
        """
        try:

            # Normalize the key
            normalized_key = EncryptionManager.normalize_key(key)

            # Create Fernet instance
            fernet = Fernet(normalized_key)

            # Decrypt the message
            decrypted = fernet.decrypt(encrypted_message.encode())

            # Return decrypted message as string
            return decrypted.decode()

        # Error during decryption: return None
        except Exception:
            return None
