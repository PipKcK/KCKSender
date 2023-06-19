import os
from statements import *

def create_file(path, filename, filedata):
    file_path = os.path.join(path, filename)  # Join path and filename safely

    # Check if the file already exists
    file_exists = os.path.exists(file_path)
    count = 1

    while file_exists:
        # Create a new filename with an incremented number
        base_name, extension = os.path.splitext(filename)
        incremented_filename = f"{base_name} ({count}){extension}"
        file_path = os.path.join(path, incremented_filename)
        count += 1

        # Check if the new filename exists
        file_exists = os.path.exists(file_path)

    with open(file_path, 'wb') as file:
        file.write(filedata)
    printg(f"File '{os.path.basename(file_path)}' created successfully at '{path}'.")
