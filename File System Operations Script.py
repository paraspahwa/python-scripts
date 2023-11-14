# Perform file system operations using os and shutil

import os
import shutil

# Create a new directory
os.mkdir('new_directory')

# Copy files from one directory to another
source_dir = 'source'
destination_dir = 'destination'
shutil.copytree(source_dir, destination_dir)

# List files in a directory
file_list = os.listdir(destination_dir)
print("Files in destination directory:", file_list)
