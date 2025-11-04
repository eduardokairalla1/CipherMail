"""
Models for User
"""

# --- TYPES ---
from bson import ObjectId
from typing import Optional


# --- CODE ---
class User:
    """
    Represents a user in the system
    """

    def __init__(self, username: str, password: str, _id: Optional[ObjectId] = None) -> None:
        """
        Initializes a User object

        :param username: Username of the user
        :param password: Password of the user
        :param _id: Optional MongoDB document ID

        :return: None
        """
        self.username = username
        self.password = password
        self._id = _id


    def to_dict(self) -> dict:
        """
        Converts user to dictionary for MongoDB

        :return: Dictionary representation of the user
        """
        # Convert user to dictionary
        user_dict = {
            'username': self.username,
            'password': self.password
        }

        # _id field present: add it to the dictionary
        if self._id is not None:
            user_dict['_id'] = self._id

        # Return the dictionary
        return user_dict


    @staticmethod
    def from_dict(data: dict) -> 'User':
        """
        Creates User object from dictionary
        
        :param data: Dictionary containing user data

        :return: User object
        """
        return User(
            username=data['username'],
            password=data['password'],
            _id=data.get('_id')
        )
