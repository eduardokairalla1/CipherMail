"""
Authentication and Registration Service
"""

# --- IMPORTS ---
from ciphermail.config.database import DatabaseManager
from ciphermail.models.user import User

import hashlib


# --- TYPES ---
from typing import Optional


# --- CODE ---
class AuthManager:
    """
    Handles user authentication and registration
    """

    def __init__(self, db_manager: DatabaseManager) -> None:
        """
        Initializes the AuthManager with a database manager

        :param db_manager: DatabaseManager instance

        :return: None
        """
        self.db_manager = db_manager
        self.users_collection = db_manager.get_users_collection()


    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes password using SHA256
        
        :param password: Plain text password

        :return: Hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()


    def register(self, username: str, password: str) -> bool:
        """
        Registers a new user

        :param username: Desired username
        :param password: Desired password

        :return: True if registration is successful, False if username exists
        """

        # User already exists: return False
        if self.users_collection.find_one({'username': username}):
            return False

        # Create new user
        user = User(username, self.hash_password(password))
        
        # Insert user into database
        self.users_collection.insert_one(user.to_dict())

        # Registration successful
        return True


    def login(self, username: str, password: str) -> Optional[User]:
        """
        Authenticates user

        :param username: Username
        :param password: Password

        :return: User object if authentication is successful, None otherwise
        """

        # Find user in database
        user_data = self.users_collection.find_one({
            'username': username,
            'password': self.hash_password(password)
        })

        # Not found user: return None
        if user_data is None:
            return None

        # Return User object
        return User.from_dict(user_data)
