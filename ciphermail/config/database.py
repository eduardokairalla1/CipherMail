"""
Database configuration and connection management
"""

# --- IMPORTS ---
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection

import os


# --- GLOBALS ---
# Load environment variables
load_dotenv()


# --- CODE ---
class DatabaseManager:
    """
    Manages MongoDB connection and operations
    """

    def __init__(self) -> None:
        """
        Initializes the DatabaseManager with MongoDB connection
        
        :return: None
        """
        connection_string = os.getenv('MONGODB_URI')
        database_name = 'ciphermail_db'
        users_collection_name = 'users'
        messages_collection_name = 'messages'

        # Initialize MongoDB connection
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.users = self.db[users_collection_name]
        self.messages = self.db[messages_collection_name]


    def close(self) -> None:
        """
        Close database connection

        :return: None
        """
        self.client.close()


    def get_users_collection(self) -> Collection:
        """
        Returns users collection

        :return: User collection
        """
        return self.users


    def get_messages_collection(self) -> Collection:
        """
        Returns messages collection

        :return: Message collection
        """
        return self.messages
