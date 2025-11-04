"""
CLI Application
"""

# --- IMPORTS ---
from colorama import Fore
from colorama import Style
from ciphermail.config.database import DatabaseManager
from ciphermail.services.auth import AuthManager
from ciphermail.services.messaging import MessagingManager
from ciphermail.models.user import User
from ciphermail.interface.ui import UI

import getpass


# --- CODE ---
class MainCLI:
    """
    Main CLI application
    """

    def __init__(self):
        """
        Initializes the CLI application
        """
        self.db_manager = DatabaseManager()
        self.auth_manager = AuthManager(self.db_manager)
        self.messaging_manager = MessagingManager(self.db_manager)
        self.current_user: User = None

        # Auth menu options
        self.auth_menu_options = {
            '1': self.login,
            '2': self.register,
            '3': self.exit_app
        }

        # Main menu options
        self.main_menu_options = {
            '1': self.send_message,
            '2': self.read_messages,
            '3': self.logout
        }


    def run(self) -> None:
        """
        Main application loop

        :return: None
        """

        # Clear screen and display welcome banner
        UI.clear_screen()
        UI.print_banner()

        # Main loop
        while True:

            # No user logged in: show auth menu
            if not self.current_user:
                self.show_auth_menu()

            # User logged in: show main menu
            else:
                self.show_main_menu()


    def show_auth_menu(self) -> None:
        """
        Shows authentication menu

        :return: None
        """

        # Display auth menu
        UI.print_section('AUTHENTICATION')
        UI.print_menu_option('1', 'Login to existing account', '🔑')
        UI.print_menu_option('2', 'Register new account', '📝')
        UI.print_menu_option('3', 'Exit system', '🚪')

        # Get user choice
        choice = UI.get_input('Choose an option: ')

        # Get action based on choice
        action = self.auth_menu_options.get(choice)

        # Invalid option: show error and exit
        if action is None:
            UI.print_error('Invalid option!')
            return

        # Execute chosen action
        action()


    def exit_app(self) -> None:
        """
        Exits the application

        :return: None
        """
        # Print goodbye message
        UI.print_goodbye()

        # Close DB connection
        self.db_manager.close()

        # Exit program
        exit(0)


    def login(self) -> None:
        """
        Handles user login

        :return: None
        """

        # Display login prompt
        UI.print_section('LOGIN')

        # Get credentials
        username = UI.get_input('Username: ')

        # Get password (hidden input)
        password = getpass.getpass(f'\033[93m▶ Password: \033[37m')

        # Attempt login
        user = self.auth_manager.login(username, password)

        # Invalid credentials: show error and exit
        if user is None:
            UI.print_error('Access denied! Invalid credentials.')
            return

        # Set current user
        self.current_user = user

        # Show success message
        UI.clear_screen()
        UI.print_success(f'Access granted! Welcome, @{username}!')


    def register(self) -> None:
        """
        Handles user registration

        :return: None
        """

        # Display registration prompt
        UI.print_section('REGISTER NEW ACCOUNT')

        # Get username
        username = UI.get_input('Username: ')

        # Get password (hidden input)
        password = getpass.getpass(f'\033[93m▶ Password: \033[37m')

        registration_result = self.auth_manager.register(username, password)

        # Registration failed: show error and exit
        if registration_result is False:
            UI.print_error('Registration failed! Username already exists.')
            return

        # Show success message
        UI.clear_screen()
        UI.print_success(f'Account @{username} created successfully! You can now login.')
        

    def show_main_menu(self) -> None:
        """
        Shows main menu for authenticated users

        :return: None
        """

        # Display main menu
        UI.print_user_status(self.current_user.username)
        UI.print_menu_option('1', 'Send encrypted message', '📨')
        UI.print_menu_option('2', 'Read my messages', '📬')
        UI.print_menu_option('3', 'Logout', '🚪')

        # Get user choice
        choice = UI.get_input('Choose an option: ')

        # Get action based on choice
        action = self.main_menu_options.get(choice)

        # Invalid option: show error and exit
        if action is None:
            UI.print_error('Invalid option!')
            return

        # Execute chosen action
        action()


    def send_message(self) -> None:
        """
        Handles sending a message

        :return: None
        """

        # Clear screen and display send message header
        UI.clear_screen()
        UI.print_section('SEND ENCRYPTED MESSAGE')

        # Get recipient username
        recipient = UI.get_input('Recipient (@username): ')

        # Recipient username starts with '@': remove @
        if recipient.startswith('@'):
            recipient = recipient[1:]

        # Get message content
        content = UI.get_input('Message: ')

        # Get encryption key (hidden input)
        encryption_key = getpass.getpass(f'\033[93m▶ Encryption key: \033[37m')

        # Send the message
        send_message_result = self.messaging_manager.send_message(self.current_user.username,
                                                                  recipient,
                                                                  content,
                                                                  encryption_key)

        # Sending failed: show error and exit
        if send_message_result is False:
            UI.print_error('Failed to send message! Please try again.')
            return

        # Show success message
        UI.clear_screen()
        UI.print_success(f'Message encrypted and sent to @{recipient}!')


    def read_messages(self) -> None:
        """
        Handles reading messages

        :return: None
        """

        # Clear screen and display messages header
        UI.clear_screen()
        UI.print_section('YOUR ENCRYPTED MESSAGES')

        # Get unread messages for current user
        messages = self.messaging_manager.get_unread_messages(self.current_user.username)

        # No messages: show info and exit
        if not messages:
            UI.print_info('No new messages. Your inbox is empty.')
            return

        # Display messages
        for idx, msg in enumerate(messages, 1):
            UI.print_menu_option(
                str(idx),
                f'From: @{msg.sender} | {msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")}',
                '🔒'
            )

        # Choose message to read
        try:

            # Get user choice
            choice = int(UI.get_input('\nSelect message number to read (0 to cancel): '))
            
            # Choice 0: cancel and return
            if choice == 0:
                UI.clear_screen()
                return

            # Invalid message number: show error and exit
            if choice < 1 or choice > len(messages):
                UI.print_error('Invalid message number!')
                return

            # Get selected message
            selected_message = messages[choice - 1]

            # Get encryption key (hidden input)
            encryption_key = getpass.getpass(f'\033[93m▶ Enter decryption key: \033[37m')

            # Attempt to decrypt the message
            decrypted_content = self.messaging_manager.read_message(
                selected_message._id,
                encryption_key
            )

            # Decryption failed: show error and exit
            if decrypted_content is None:
                UI.print_error('Decryption failed! Wrong key or corrupted message.')
                return

            # Display decrypted message            
            UI.clear_screen()
            UI.print_message_header(
                selected_message.sender,
                selected_message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            )
            UI.print_message_content(decrypted_content)

            # Wait for user to press Enter to continue
            input(f'{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

            # Clear screen after reading message
            UI.clear_screen()

        # Invalid input (non-integer): show error
        except ValueError:
            UI.print_error('Invalid input! Please enter a number.')


    def logout(self) -> None:
        """
        Logs out current user

        :return: None
        """

        # Clear screen and show goodbye message
        UI.clear_screen()
        UI.print_goodbye(self.current_user.username)

        # Clear current user
        self.current_user = None
