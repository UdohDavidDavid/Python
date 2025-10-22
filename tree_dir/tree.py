# Also david, if theres something you want to implement like this tree stuff,
# Just search up a library for it

from treelib import Tree # import Treelib
import argparse
import os
import sys

# Creates a new tree
tree = Tree()

# Create a new tree
tree.create_node("Home", "home") # Creates a root - It does not have a third argument that specifies a parent, so it is the root

# Adding departments
tree.create_node("Music", "music", parent="home") # Creates a child dir AKA Department
tree.create_node("Download", "down", parent="home")
tree.create_node("Documents", "docs", parent="home")
tree.create_node("Videos", "vid", parent="home")

# Adding team members
# This ones are under the departments
tree.create_node("Anime", "anime", parent="vid")
tree.create_node("Movies", "mov", parent="vid")
tree.create_node("Files", "file", parent="docs")
tree.create_node("tree.exe", "tree", parent="down")
tree.create_node("Washing Mashine Heart", "washing", parent="music")

# Show the tree
tree.show()

parser = argparse.ArgumentParser(
                    prog='Folder Tree',
                    description='This program prints a tree of the current directory specified or the directory specified',
                    epilog='Use --help to request help message')

parser.add_argument('-f', '--folder')
args = parser.parse_args()

current_args = sys.argv

def printhomedir():
    cwd = os.getcwd()
    print(cwd)
    tree = Tree()
    tree.create_node(cwd, cwd)

    for file in os.listdir(cwd):
        fullpath = os.path.join(cwd, file)
        if os.path.isdir(fullpath):
            if not tree.contains(file):
                tree.create_node(file, file, parent=cwd)
                for folder in os.listdir(fullpath):
                    if not tree.contains(folder):
                        tree.create_node(folder, folder, parent=file)
        elif os.path.isfile(fullpath):
            tree.create_node(file, file, parent=cwd)
    tree.show()

def printdir():
    cwd = args.folder
    print(cwd)
    tree = Tree()
    tree.create_node(cwd, cwd)

    for file in os.listdir(cwd):
        fullpath = os.path.join(cwd, file)
        if os.path.isdir(fullpath):
            if not tree.contains(file):
                tree.create_node(file, file, parent=cwd)
                for folder in os.listdir(fullpath):
                    if not tree.contains(folder):
                        tree.create_node(folder, folder, parent=file)
        elif os.path.isfile(fullpath):
            tree.create_node(file, file, parent=cwd)
    tree.show()

if args.folder == None:
    printhomedir()

elif args.folder != None:
    printdir()
