import os
import time

# Define the directory where the PDF files are located
pdf_dir = './'

# Get the current time
current_time = time.time()

# Iterate over the files in the directory
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        # Get the path to the file
        file_path = os.path.join(pdf_dir, filename)
        
        # Get the time when the file was created
        file_creation_time = os.path.getctime(file_path)
        
        # Check if the file was created more than 5 minutes ago
        if current_time - file_creation_time > 60:  # 300 seconds = 5 minutes
            # If the file was created more than 5 minutes ago, delete it
            os.remove(file_path)