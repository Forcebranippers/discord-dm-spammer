from __future__ import annotations

from colorama import Fore, Style, init as colorama_init
from pyfiglet import Figlet

colorama_init(autoreset=True)


def banner(text: str = "DM SPAMMER") -> str:
    fig = Figlet(font="small")
    art = fig.renderText(text)
    colored = f"{Fore.MAGENTA}{art}{Style.RESET_ALL}"
    print(colored)
    print(f"{Fore.CYAN}discord-dm-spammer :: 2026 edition{Style.RESET_ALL}\n")
    return art