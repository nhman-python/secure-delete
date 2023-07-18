import argparse
import os
from art import text2art

class Colors:
    """ANSI escape sequences for color"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def secure_delete(file_path, strong=1):
    """Securely deletes a file by overwriting it multiple times."""
    if os.path.isfile(file_path):
        q = input(f'{Colors.YELLOW}[?] Are you sure you want to continue? This will delete your file without an '
                  f'option to restore it. (y/n) {Colors.RESET}')
        if q.lower() == 'y':
            print(f'{Colors.YELLOW}[-] Starting secure deletion of the file. Please wait a minute...{Colors.RESET}')
            data = os.urandom(1024)
            size = os.path.getsize(file_path)
            num_loop = size // 1024
            remaining_bytes = num_loop % 1024

            try:
                for _ in range(strong):
                    with open(file_path, 'wb') as f:
                        for _ in range(num_loop):
                            f.write(data)

                        f.write(data[:remaining_bytes])

                os.remove(file_path)
                print(f'{Colors.GREEN}[!] The file {file_path} has been securely deleted!{Colors.RESET}')

            except (PermissionError, ValueError, KeyboardInterrupt) as err:
                print(f'{Colors.RED}{err}{Colors.RESET}')
        else:
            print(f'{Colors.RED}[x] Cancel the delete{Colors.RESET}')
    else:
        print(f'{Colors.RED}[?] The provided path is not a file or does not exist!{Colors.RESET}')


def main():
    """Entry point of the script"""
    banner = text2art('secure delete')
    ascii_banner = f'{Colors.RED}{banner}{Colors.GREEN}\t\t\t\twrite by @github.com/nhman-python{Colors.RESET}\n'
    print(ascii_banner)

    parser = argparse.ArgumentParser(prog='Secure File Deletion',
                                     description='This script helps you securely delete a file '
                                                 'by overwriting it multiple times.')
    parser.add_argument('file_path', type=str, help='The path to the file that you want to delete securely.')
    parser.add_argument('strong', type=int, help='The number of overwrite passes to make on the file. '
                                                 'Higher values increase security but take more time. '
                                                 'Recommend 4.')
    args = parser.parse_args()
    secure_delete(args.file_path, args.strong)


if __name__ == '__main__':
    main()
