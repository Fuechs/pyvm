from colorama import Fore as c

def throw(message: str = "no message", location: int = -1):
    print(f"[{c.RED} ERROR {c.RESET}]: {message} [at ROM:{location:04d}]")
    exit(location)