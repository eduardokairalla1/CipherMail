"""
CLI UI Components
"""

# --- IMPORTS ---
from colorama import Fore
from colorama import Style
from colorama import init

import os


# --- GLOBALS ---
# Initialize colorama
init(autoreset=True)


# --- CODE ---
class UI:
    """
    UI/UX components for the CLI
    """

    @staticmethod
    def clear_screen() -> None:
        """
        Clears the terminal screen
        
        :return: None
        """
        os.system('clear' if os.name != 'nt' else 'cls')


    @staticmethod
    def print_banner() -> None:
        """
        Prints the welcome banner

        :return: None
        """

        # ASCII Art Banner
        banner = f"""
{Fore.GREEN}╔════════════════════════════════════════════════════════════════════╗
║  {Fore.CYAN} ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗                        {Fore.GREEN}║
║  {Fore.CYAN}██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗                       {Fore.GREEN}║
║  {Fore.CYAN}██║     ██║██████╔╝███████║█████╗  ██████╔╝                       {Fore.GREEN}║
║  {Fore.CYAN}██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗                       {Fore.GREEN}║
║  {Fore.CYAN}╚██████╗██║██║     ██║  ██║███████╗██║  ██║                       {Fore.GREEN}║
║  {Fore.CYAN} ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                       {Fore.GREEN}║
║                                                                    ║
║  {Fore.YELLOW}███╗   ███╗ █████╗ ██╗██╗                                         {Fore.GREEN}║
║  {Fore.YELLOW}████╗ ████║██╔══██╗██║██║                                         {Fore.GREEN}║
║  {Fore.YELLOW}██╔████╔██║███████║██║██║                                         {Fore.GREEN}║
║  {Fore.YELLOW}██║╚██╔╝██║██╔══██║██║██║                                         {Fore.GREEN}║
║  {Fore.YELLOW}██║ ╚═╝ ██║██║  ██║██║███████╗                                    {Fore.GREEN}║
║  {Fore.YELLOW}╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝                                    {Fore.GREEN}║
║                                                                    ║
║                {Fore.RED}[{Fore.WHITE} ENCRYPTED • ANONYMOUS • SECURE {Fore.RED}]{Fore.GREEN}                  ║
║                  {Fore.MAGENTA}Developed by Eduardo Kairalla{Fore.GREEN}                     ║
╚════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

        # Print the banner
        print(banner)


    @staticmethod
    def print_section(title: str) -> None:
        """
        Prints a section header

        :return: None
        """
        print(f'\n{Fore.CYAN}{'═' * 70}')
        print(f'{Fore.YELLOW}▶ {title}')
        print(f'{Fore.CYAN}{'═' * 70}{Style.RESET_ALL}')


    @staticmethod
    def print_menu_option(number: str, text: str, icon: str = '→') -> None:
        """
        Prints a menu option

        :return: None
        """
        print(f'{Fore.GREEN}[{number}]{Fore.WHITE} {icon} {text}{Style.RESET_ALL}')


    @staticmethod
    def print_success(message: str) -> None:
        """
        Prints a success message

        :return: None
        """
        print(f'\n{Fore.GREEN}✓ {message}{Style.RESET_ALL}')


    @staticmethod
    def print_error(message: str) -> None:
        """
        Prints an error message

        :return: None
        """
        print(f'\n{Fore.RED}✗ {message}{Style.RESET_ALL}')


    @staticmethod
    def print_info(message: str) -> None:
        """
        Prints an info message

        :return: None
        """
        print(f'\n{Fore.CYAN}ℹ {message}{Style.RESET_ALL}')


    @staticmethod
    def print_warning(message: str) -> None:
        """
        Prints a warning message

        :return: None
        """
        print(f'\n{Fore.YELLOW}⚠ {message}{Style.RESET_ALL}')


    @staticmethod
    def print_message_header(sender: str, date: str) -> None:
        """
        Prints a message header

        :return: None
        """
        print(f'\n{Fore.CYAN}{'═' * 70}')
        print(f'{Fore.GREEN}FROM:{Fore.WHITE} @{sender}')
        print(f'{Fore.GREEN}DATE:{Fore.WHITE} {date}')
        print(f'{Fore.CYAN}{'═' * 70}{Style.RESET_ALL}')


    @staticmethod
    def print_message_content(content: str) -> None:
        """
        Prints message content

        :return: None
        """
        print(f'{Fore.WHITE}{content}')
        print(f'{Fore.CYAN}{'═' * 70}{Style.RESET_ALL}\n')


    @staticmethod
    def print_user_status(username: str) -> None:
        """
        Prints logged in user status

        :return: None
        """
        print(f'\n{Fore.MAGENTA}{'━' * 70}')
        print(f'{Fore.YELLOW}⚡ LOGGED IN AS:{Fore.GREEN} @{username} {Fore.YELLOW}⚡')
        print(f'{Fore.MAGENTA}{'━' * 70}{Style.RESET_ALL}')


    @staticmethod
    def get_input(prompt: str) -> str:
        """
        Gets user input with styled prompt

        :return: User input string
        """
        return input(f'{Fore.YELLOW}▶ {prompt}{Fore.WHITE}').strip()


    @staticmethod
    def print_goodbye(username: str = None) -> None:
        """
        Prints goodbye message

        :return: None
        """

        # Username provided: personalized goodbye
        if username:
            print(f'\n{Fore.CYAN}◈ {Fore.WHITE}Goodbye, {Fore.GREEN}@{username}{Fore.WHITE}! '
                  f'Stay secure!{Fore.CYAN}◈{Style.RESET_ALL}\n')

            # Exit
            return
        
        # Generic goodbye message
        print(f'\n{Fore.CYAN}◈ {Fore.WHITE}Connection terminated. Stay anonymous! {Fore.CYAN}◈{Style.RESET_ALL}\n')
