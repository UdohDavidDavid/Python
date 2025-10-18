###########################################################
# This script only works for the Downloads folder because
# it is usually the most unorganised.

# It is also only for the Downloads folder so that project files and 
# other files wont be accedentally moved around

# Author: David

# Note: The commented part at the bottom of the file was a demo to move around
# some font file that filled my downloads folder and is what sparked the idea for
# this project.

import os       # For performing operations with files in this case
import shutil   # Used to move files to other directories
import argparse # Doesnt have a use case other than providing help

parser = argparse.ArgumentParser(
    prog = "File Sort",
    description = "Sorts files based on type - E.g, Music, Videos, Compressed, Fonts. Just go to folder you wish to sort and run the program",
    epilog = "Use --help to show help message",
) # The parser provides help information

file_types = { # All types of files and the folder they will be moved to
    ".ttf" : "Fonts",
    ".mp3" : "Music",
    ".mp4" : "Videos",
    ".jpg" : "Pictures",
    ".png" : "Pictures",
    ".rar" : "Compressed",
    ".zip" : "Compressed",
    ".tar" : "Compressed",
    ".exe" : "App",
    ".bin" : "App",
    ".jar" : "App",
    ".deb" : "App",
    ".apk" : "App",
}             # some of the filetypes listed here are not native to one operating system


working_dir = os.path.join(os.path.expanduser("~"), "Downloads")  # The working directory defaults to the Downloads folder

for file_type, folder in file_types.items(): # The file type and folder in key, value pairs
    for files in os.listdir(working_dir):    # Checks all files in working directory
        fullpath = os.path.join(working_dir, files)  #Gets all files and folders in working directory
        if os.path.isfile(fullpath) and files.endswith(file_type): # Checks that it is a file (Ignores Folders) and checks format of file
            if not os.path.isdir(folder):    # Checks if directory already exists
                os.mkdir(os.path.join(working_dir, folder))  # If directory is absent, it creates one
            shutil.move(fullpath, os.path.join(working_dir, folder)) # Moves files to new folders




############### Demo script ###############
#ttf_file = []
#ttf_dir = []
#
#for file in os.listdir(working_dir):
#    full_path = os.path.join(working_dir, file)
#    if os.path.isfile(full_path) and file.endswith(".ttf"):
#        ttf_file.append(file)
#for file in ttf_file:
#    ttf_dir.append(os.path.join(working_dir, file))
#
#new_dir = "Fonts"
#if not os.path.isdir(new_dir):
#    os.mkdir(os.path.join(working_dir, new_dir))
#new_dir_path = os.path.join(working_dir, new_dir)
#print(new_dir_path)
#
#for file in ttf_dir:
#    shutil.move(file, new_dir_path)
