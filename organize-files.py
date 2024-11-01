import os
import shutil

# Set the path to your Downloads folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
# Define the path for the resume-in-downloads folder
resume_folder_path = os.path.join(downloads_path, 'resume-in-downloads')


# Define folder paths for each file type
folder_paths = {
    'pdf': os.path.join(downloads_path, 'unorganized_pdf'),
    'epub': os.path.join(downloads_path, 'unorganized_epub'),
    'zip': os.path.join(downloads_path, 'unorganized_zip'),
    'txt': os.path.join(downloads_path, 'unorganized_txt'),
    'md': os.path.join(downloads_path, 'unorganized_md'),
    'mobi': os.path.join(downloads_path, 'unorganized_mobi'),
      'jpeg': os.path.join(downloads_path, 'unorganized_jpeg'),
        'png': os.path.join(downloads_path, 'unorganized_png')

}

# Create the destination folders if they do not exist
for folder_path in folder_paths.values():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move each file type to its corresponding folder
for file_name in os.listdir(downloads_path):
    for file_type, folder_path in folder_paths.items():
        if file_name.endswith('.' + file_type):
            shutil.move(os.path.join(downloads_path, file_name), folder_path)
            print(f"Moved {file_name} to {folder_path}")