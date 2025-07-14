# small python code to backup files older than 7 days
import os   
import time
import shutil

source_dir = 'path/to/your/input/directory'  # Specify the directory to check for old files
backup_dir = 'path/to/your/backup/directory'  # Specify the directory to backup old files
# Call the function to backup old files


def backup_old_files(source_dir, backup_dir): # Function to backup files older than 7 days
    if not os.path.exists(backup_dir): # Check if backup directory exists
        os.makedirs(backup_dir) # Create backup directory if it does not exist

    current_time = time.time() # Get the current time in seconds since epoch
    seven_days = 7 * 24 * 60 * 60  # seconds in 7 days

    for filename in os.listdir(source_dir): # Iterate through files in the source directory
        file_path = os.path.join(source_dir, filename) # Get the full path of the file
        if os.path.isfile(file_path): # Check if it is a file
            file_age = current_time - os.path.getmtime(file_path)   # Get the age of the file
            if file_age > seven_days: # If the file is older than 7 days
                shutil.copy(file_path, backup_dir) # Copy the file to the backup directory
                print(f"Backed up: {filename}") # Print the name of the backed up file