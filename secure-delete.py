import argparse
import os
import art
import random
import string

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def secure_delete(file_path: str, strong: int = 1) -> None:
    """
    Securely deletes a file by overwriting it multiple times and renaming it with random names.
    """
    if os.path.isfile(file_path):
        user_input = input(f'{YELLOW}[?] Are you sure you want to continue? '
                           f'This will delete your file without '
                           f'an option to restore it. (y/n) {RESET}')
        if user_input.lower() == 'y':
            print(f'{YELLOW}[-] Starting secure deletion of the file. '
                  f'Please wait a moment...{RESET}')
            
            # Renaming the file with random names
            for _ in range(strong):
                random_name = ''.join(random.choices(string.ascii_letters, k=8))
                renamed_file_path = os.path.join(os.path.dirname(file_path), random_name)
                os.rename(file_path, renamed_file_path)

                # Overwriting the renamed file with random data
                try:
                    with open(renamed_file_path, 'wb') as file:
                        file.write(os.urandom(os.path.getsize(renamed_file_path)))
                    
                except (PermissionError, ValueError, KeyboardInterrupt) as err:
                    print(f'{RED}{err}{RESET}')

            # Truncating the file before final deletion
            try:
                with open(renamed_file_path, 'wb') as file:
                    file.truncate()

                os.remove(renamed_file_path)
                print(f'{GREEN}[!] The file {file_path} has been securely deleted!{RESET}')

            except (PermissionError, ValueError, KeyboardInterrupt) as err:
                print(f'{RED}{err}{RESET}')
        else:
            print(f'{RED}[x] Cancel the delete{RESET}')
    else:
        print(f'{RED}[?] The provided path is not a file or does not exist!{RESET}')

def main() -> None:
    """
    Entry point of the script
    """
    banner = art.text2art('Secure Delete')
    ascii_banner = f'{RED}{banner}{GREEN}\t\t\t\tWritten by @github.com/nhman-python{RESET}\n'
    print(ascii_banner)

    parser = argparse.ArgumentParser(prog='Secure File Deletion',
                                     description='This script helps you securely delete a file '
                                                 'by overwriting it multiple times and renaming it with random names.')
    parser.add_argument('file_path',
                        type=str,
                        help='The path to the file that you want to delete securely.')
    parser.add_argument('strong',
                        type=int,
                        help='The number of overwrite passes to make on the file. '
                             'Higher values increase security but take more time. '
                             'Recommended value is 4.')
    args = parser.parse_args()
    secure_delete(args.file_path, args.strong)

if __name__ == '__main__':
    main()
