"""
Messaging service
"""

# --- IMPORTS ---
from datetime import datetime
from ciphermail.config.database import DatabaseManager
from ciphermail.models.message import Message
from ciphermail.services.encryption import EncryptionManager


# --- TYPES ---
from typing import List
from typing import Optional


# --- CODE ---
class MessagingManager:
    """
    Handles message operations
    """

    def __init__(self, db_manager: DatabaseManager) -> None:
        """
        Initializes the MessagingManager with a database manager

        :param db_manager: DatabaseManager instance

        :return: None
        """
        self.db_manager = db_manager
        self.messages_collection = db_manager.get_messages_collection()
        self.encryption_manager = EncryptionManager()


    def send_message(self, sender: str, recipient: str, content: str, encryption_key: str) -> bool:
        """
        Sends an encrypted message

        :param sender: Sender's username
        :param recipient: Recipient's username
        :param content: Message content
        :param encryption_key: Key to encrypt the message

        :return: True if sent successfully, False otherwise
        """
        try:

            # Get users collection
            users_collection = self.db_manager.get_users_collection()

            # Verify recipient exists
            if not users_collection.find_one({'username': recipient}):
                return False

            # Encrypt content
            encrypted_content = self.encryption_manager.encrypt(content, encryption_key)

            # Create message object
            message = Message(
                sender=sender,
                recipient=recipient,
                encrypted_content=encrypted_content,
                timestamp=datetime.now(),
                read=False
            )
            
            # Store message in database
            self.messages_collection.insert_one(message.to_dict())

            # Return success
            return True
        
        # Errors during encryption or database operations: print and return False
        except Exception as e:
            print(f'Error sending message: {e}')
            return False


    def get_unread_messages(self, username: str) -> List[Message]:
        """
        Gets all unread messages for a user

        :param username: Recipient's username

        :return: List of unread Message objects
        """

        # Query unread messages
        messages_data = self.messages_collection.find({
            'recipient': username,
            'read': False
        }).sort('timestamp', -1)

        # Return list of Message objects
        return [Message.from_dict(msg) for msg in messages_data]


    def read_message(self, message_id, encryption_key: str) -> Optional[str]:
        """
        Reads and decrypts a message, marks it as read

        :param message_id: ID of the message to read
        :param encryption_key: Key to decrypt the message

        :return: Decrypted message content, or None if not found/decryption fails
        """

        # Fetch message from database
        message_data = self.messages_collection.find_one({'_id': message_id})

        # If message not found, return None
        if not message_data:
            return None

        # Convert to Message object
        message = Message.from_dict(message_data)

        # Decrypt content
        decrypted_content = self.encryption_manager.decrypt(
            message.encrypted_content,
            encryption_key
        )

        # If decryption successful: mark message as read
        if decrypted_content:

            # Mark as read
            self.messages_collection.update_one(
                {'_id': message_id},
                {'$set': {'read': True}}
            )

        # Return decrypted content
        return decrypted_content
