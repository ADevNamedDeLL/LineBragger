import os
import shutil
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore

init(autoreset=True)

# Color definitions
WHITE = Fore.WHITE
RED = Fore.RED
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
GREEN = Fore.GREEN
CYAN = Fore.CYAN

RAINBOW = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

EXCLUDED_DIRS = {'node_modules', '.git', '__pycache__'}
EXCLUDED_FILES = {'package.json', 'package-lock.json', 'yarn.lock'}

PROGRAMMING_EXTENSIONS = {
    '.py', '.js', '.ts', '.java', '.cpp', '.c', '.cs', '.html', '.css',
    '.go', '.rs', '.php', '.rb', '.swift', '.kt', '.sh', '.json'
}

# Clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Center and print the rainbow ASCII logo
def rainbow_ascii_logo():
    logo_lines = [
        "/$$       /$$                     /$$$$$$$                                                                  ",
        "| $$      |__/                    | $$__  $$                                                                 ",
        "| $$       /$$ /$$$$$$$   /$$$$$$ | $$  \\ $$  /$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$       ",
        "| $$      | $$| $$__  $$ /$$__  $$| $$$$$$$  /$$__  $$|____  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$      ",
        "| $$      | $$| $$  \\ $$| $$$$$$$$| $$__  $$| $$  \\__/ /$$$$$$$| $$  \\ $$| $$  \\ $$| $$$$$$$$| $$  \\__/      ",
        "| $$      | $$| $$  | $$| $$_____/| $$  \\ $$| $$      /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$            ",
        "| $$$$$$$$| $$| $$  | $$|  $$$$$$$| $$$$$$$/| $$     |  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$            ",
        "|________/|__/|__/  |__/ \\_______/|_______/ |__/      \\_______/ \\____  $$ \\____  $$ \\_______/|__/            ",
        "                                                                /$$  \\ $$ /$$  \\ $$                          ",
        "                                                               |  $$$$$$/|  $$$$$$/                          ",
        "                                                                \\______/  \\______/                           "
    ]
    width = shutil.get_terminal_size().columns
    print('\n' * 1)  # Top margin

    for i, line in enumerate(logo_lines):
        color = RAINBOW[i % len(RAINBOW)]
        print(color + line.center(width))

def print_menu():
    print(MAGENTA + "\n=== Main Menu ===".center(shutil.get_terminal_size().columns))
    print(WHITE + "[1] Brag")
    print(WHITE + "[2] About")
    print(WHITE + "[0] Exit")

def about():
    print(MAGENTA + "\nAbout:")
    print(WHITE + "This script scans your programming folders and tells you how much code you've written!")
    print(WHITE + "So you can go and " + GREEN + "Brag" + WHITE + " about it")
    print(WHITE + "Created by " + CYAN + "a Dev Named DeLL")

def is_code_file(file):
    return os.path.splitext(file)[1] in PROGRAMMING_EXTENSIONS

def scan_folder(folder_path):
    total_files = 0
    total_folders = 0
    total_lines = 0
    total_chars = 0

    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        total_folders += len(dirs)

        for file in files:
            if file in EXCLUDED_FILES:
                continue

            full_path = os.path.join(root, file)
            if is_code_file(file):
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        lines = content.splitlines()
                        total_lines += len(lines)
                        total_chars += len(content)
                        total_files += 1
                except Exception as e:
                    print(RED + f"Error reading {file}: {e}")

    return total_folders, total_files, total_lines, total_chars

def brag():
    print(YELLOW + "[TODO] Choose a folder to analyze:")
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    if not folder_selected:
        print(RED + "No folder selected!")
        input(WHITE + "\nPress Enter to return...")
        return

    print(YELLOW + f"Analyzing: {folder_selected} ...")
    folders, files, lines, chars = scan_folder(folder_selected)

    print(WHITE + "\nWhat would you like to see?")
    print(WHITE + "[1] Total lines of code")
    print(WHITE + "[2] Total characters written")
    choice = input(WHITE + "Choice: ")

    clear()
    rainbow_ascii_logo()
    print(MAGENTA + "\n=== Brag Stats ===")
    print(WHITE + f"Folders scanned: {folders}")
    print(WHITE + f"Files scanned:   {files}")

    if choice == '1':
        print(WHITE + f"Total lines of code: {lines}")
    elif choice == '2':
        print(WHITE + f"Total characters written: {chars}")
    else:
        print(RED + "Invalid choice!")

    input(WHITE + "\nPress Enter to return to menu...")

def main():
    while True:
        clear()
        rainbow_ascii_logo()
        print_menu()
        choice = input(WHITE + "\nSelect an option: ")

        if choice == '1':
            clear()
            rainbow_ascii_logo()
            brag()
        elif choice == '2':
            clear()
            rainbow_ascii_logo()
            about()
            input(WHITE + "\nPress Enter to return to menu...")
        elif choice == '0':
            clear()
            print(WHITE + "Goodbye!")
            break
        else:
            print(RED + "Invalid option!")
            input(WHITE + "\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
