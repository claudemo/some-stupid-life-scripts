import os
from PIL import Image

# Get the current working directory
cwd = os.getcwd()

# Find all PNG files in the current directory
png_files = [file for file in os.listdir(cwd) if file.endswith('.png')]

# Sort files if needed (optional, based on file names)
png_files.sort()

# Open the images and convert them to RGB
images = [Image.open(png).convert('RGB') for png in png_files]

# Save as PDF
if images:
    images[0].save("output.pdf", save_all=True, append_images=images[1:])
    print("PDF created successfully!")
else:
    print("No PNG files found.")
    