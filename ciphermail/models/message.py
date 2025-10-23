"""
Models for Message
"""

# --- IMPORTS ---
from datetime import datetime


# --- TYPES ---
from bson import ObjectId
from typing import Optional


# --- CODE ---
class Message:
    """
    Represents a message in the system
    """

    def __init__(self,
                 sender: str,
                 recipient: str,
                 encrypted_content: str,
                 timestamp: Optional[datetime] = None,
                 read: bool = False,
                 _id: Optional[ObjectId] = None) -> None:
        """
        Initializes a Message object

        :param sender: Sender's username
        :param recipient: Recipient's username
        :param encrypted_content: Encrypted message content
        :param timestamp: Timestamp of the message
        :param read: Read status of the message
        :param _id: Optional MongoDB document ID

        :return: None
        """
        self.sender = sender
        self.recipient = recipient
        self.encrypted_content = encrypted_content
        self.timestamp = timestamp or datetime.now()
        self.read = read
        self._id = _id


    def to_dict(self) -> dict:
        """
        Converts message to dictionary for MongoDB

        :return: Dictionary representation of the message
        """

        # Convert message to dictionary
        message_dict = {
            'sender': self.sender,
            'recipient': self.recipient,
            'encrypted_content': self.encrypted_content,
            'timestamp': self.timestamp,
            'read': self.read
        }

        # _id field present: add it to the dictionary
        if self._id is not None:
            message_dict['_id'] = self._id

        # Return the dictionary
        return message_dict


    @staticmethod
    def from_dict(data: dict) -> 'Message':
        """
        Creates Message object from dictionary
        
        :param data: Dictionary containing message data

        :return: Message object
        """
        return Message(
            sender=data['sender'],
            recipient=data['recipient'],
            encrypted_content=data['encrypted_content'],
            timestamp=data['timestamp'],
            read=data.get('read', False),
            _id=data.get('_id')
        )
