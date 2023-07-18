
   # Secure File Deletion Script

   ![Secure File Deletion Banner](https://github.com/nhman-python/secure-delete/blob/main/logo.png)

   ## Description

   This script securely deletes a file by overwriting its contents multiple times, ensuring that it cannot be easily recovered. It provides an option to delete files without the possibility of restoration.

   ## Usage

   ```
   python secure-delete.py file_path strong
   ```

   Arguments:
   - `file_path`: The path to the file that you want to delete securely.
   - `strong`: The number of overwrite passes to make on the file. Higher values increase security but take more time. Recommended value is 4.

   ## Installation

   1. Clone the repository:
      ```
      git clone https://github.com/nhman-python/secure-delete.git
      ```

   2. Change to the project directory:
      ```
      cd secure-delete
      ```

   ## Examples

   Securely delete a file:
   ```shell
   python3 secure-delete.py file.txt 4
   ```
   windows:
   ```shell
   python secure-delete.py file.txt 4
   ```

   ## License

   [MIT License](https://github.com/nhman-python/secure-delete/blob/main/LICENSE)

   ## Contributing

   ## Credits

   - Author: [@github.com/nhman-python](https://github.com/nhman-python)
