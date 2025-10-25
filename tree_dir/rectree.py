# Author: David

import os # os.path for files and stuff
import argparse # command line parser
from treelib import Tree


parser = parser = argparse.ArgumentParser(
                    prog='Recursive Tree',
                    description='Recursively prints directories',
                    epilog='Try --help for help')

parser.add_argument('-f''--folder', help="Type int please")
args = parser.parse_args()

path = os.path.join(os.getcwd()) # Get current dir


# Function to build tree
def build_tree(path):
    tree = Tree() # Creates the tree
    tree.create_node(os.path.basename(path), path)  # Creates the root node

    for root, dir, files in os.walk(path): # Gets the root, dir, and files
        for d in dir:
            dirname = os.path.join(root, d)
            tree.create_node(d, dirname, parent=root)   # Add directories to root node, files under this dir, will automatically connect to this node
        for f in files:
            filename = os.path.join(root, f)
            tree.create_node(f, filename, parent=root)   # Files will automatically connect to dir, because their root is also the directories name. Do you see the trick there, i hope you do
    # Returns the tree


if args.f__folder:
    folder = os.path.join(args.f__folder)
    tree = build_tree(folder) # Builds the tree - This could take a while for deeper roots
    tree.show() # Displays the tree
else:
    tree = build_tree(path)
    tree.show()
