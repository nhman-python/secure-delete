"""
will delete you're file securely to protect yor file from restore software
"""
import argparse
import os
import art

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'


def secure_delete(file_path: str, strong: int = 1) -> None:
    """Securely deletes a file by overwriting it multiple times."""
    if os.path.isfile(file_path):
        user_input = input(f'{YELLOW}[?] Are you sure you want to continue? '
                           f'This will delete your file without '
                           f'an option to restore it. (y/n) {RESET}')
        if user_input.lower() == 'y':
            print(f'{YELLOW}[-] Starting secure deletion of the file.'
                  f' Please wait a minute...{RESET}')
            data = os.urandom(1024)
            file_size = os.path.getsize(file_path)
            num_loops = file_size // 1024
            remaining_bytes = num_loops % 1024

            try:
                for _ in range(strong):
                    with open(file_path, 'wb') as file:
                        for _ in range(num_loops):
                            file.write(data)

                        file.write(data[:remaining_bytes])

                os.remove(file_path)
                print(f'{GREEN}[!] The file {file_path} has been securely deleted!{RESET}')

            except (PermissionError, ValueError, KeyboardInterrupt) as err:
                print(f'{RED}{err}{RESET}')
        else:
            print(f'{RED}[x] Cancel the delete{RESET}')
    else:
        print(f'{RED}[?] The provided path is not a file or does not exist!{RESET}')


def main() -> None:
    """Entry point of the script"""
    banner = art.text2art('secure delete')
    ascii_banner = f'{RED}{banner}{GREEN}\t\t\t\twrite by @github.com/nhman-python{RESET}\n'
    print(ascii_banner)

    parser = argparse.ArgumentParser(prog='Secure File Deletion',
                                     description='This script helps you securely delete a file '
                                                 'by overwriting it multiple times.')
    parser.add_argument('file_path',
                        type=str,
                        help='The path to the file that you want to delete securely.')
    parser.add_argument('strong',
                        type=int,
                        help='The number of overwrite passes to make on the file. '
                             'Higher values increase security but take more time. '
                             'Recommend 4.')
    args = parser.parse_args()
    secure_delete(args.file_path, args.strong)


if __name__ == '__main__':
    main()
