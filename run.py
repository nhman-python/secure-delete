import argparse
import os


# ANSI escape sequences for color
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'


ascii_banner = f"""
{Colors.RED}                                     _      _      _       
                                    | |    | |    | |      
  ___  ___  ___ _   _ _ __ ___    __| | ___| | ___| |_ ___ 
 / __|/ _ \/ __| | | | '__/ _ \  / _` |/ _ \ |/ _ \ __/ _ \\
 \__ \  __/ (__| |_| | | |  __/ | (_| |  __/ |  __/ ||  __/
 |___/\___|\___|\__,_|_|  \___|  \__,_|\___|_|\___|\__\___|
                                    {Colors.GREEN}write by @github.com/nhman-python{Colors.RESET}
"""
print(ascii_banner)


def secure_delete(file_path, strong=1):
    if os.path.isfile(file_path):
        q = input(Colors.YELLOW + '[?] Are you sure you want to continue? This will delete your file without an '
                                  'option to restore it. (y/n) ' + Colors.RESET)
        if q.lower() == 'y':
            print(Colors.YELLOW + '[-] Starting secure deletion of the file. Please wait a minute...' + Colors.RESET)
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
                print(Colors.GREEN + f'[!] The file {file_path} has been securely deleted!' + Colors.RESET)

            except (PermissionError, ValueError, KeyboardInterrupt) as err:
                print(Colors.RED + str(err) + Colors.RESET)
        else:
            print(Colors.RED + '[x] cancel the delete' + Colors.RESET)
    else:
        print(Colors.RED + "[?] The provided path is not a file or does not exist!" + Colors.RESET)


def main():
    parser = argparse.ArgumentParser(prog='Secure File Deletion',
                                     description='This script helps you securely delete a file '
                                                 'by overwriting it multiple times.')
    parser.add_argument('file_path', type=str, help='The path to the file that you want to delete securely.')
    parser.add_argument('strong', type=int, help='The number of overwrite passes to make on the file. '
                                                 'Higher values increase security but take more time.'
                                                 'recommend 4')
    args = parser.parse_args()
    secure_delete(args.file_path, args.strong)


if __name__ == '__main__':
    main()
