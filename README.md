# secure-delete
This script securely deletes a file by overwriting its contents multiple times. It ensures that the file cannot be easily recovered by performing a series of overwrite passes. The number of passes can be specified by the user.

To use the script, provide the path to the file you want to delete securely and the number of overwrite passes to make. The higher the number of passes, the more secure the deletion, but it will take longer to complete.

Please note that secure deletion is irreversible, and once the file is deleted, it cannot be recovered. Use this script with caution and ensure that you have selected the correct file for deletion.

Usage: python secure_file_deletion.py file_path strong

Arguments:
  file_path: The path to the file that you want to delete securely.
  strong: The number of overwrite passes to make on the file. Higher values increase security but take more time. Recommended value is 4.

