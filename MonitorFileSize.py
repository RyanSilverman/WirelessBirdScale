import os

# Set the path of the folder you want to monitor
folder_path = '/home/pi/Desktop/EEE4113F_Project/Data'

# Set the maximum size (in bytes) of the folder before files start to get deleted
#max_size = 4.8E10  # set to 48 GB (can be edited to suit users needs, 48GB was chosen arbitrarily assuming a 64 GB SD card is used)
max_size = 30E6
# Define a function to get the size of a folder
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

folder_size = get_folder_size(folder_path)
if folder_size > max_size:
    # Get a list of all files in the folder
    all_files = [(os.path.join(dp, f), os.stat(os.path.join(dp, f)).st_mtime) 
                    for dp, dn, filenames in os.walk(folder_path) 
                    for f in filenames]
    
    # Sort the list by modification time (oldest files first)
    all_files.sort(key=lambda x: x[1])
    # Delete the oldest files until the folder size is below the maximum
    for file_path, _ in all_files:
        if folder_size <= max_size:
            break
        print(f"Deleting {file_path}")
        folder_size -= os.path.getsize(file_path)
        os.remove(file_path)
