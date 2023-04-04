import sys
import os

# Makes sure the number of arguments are correct
def check_args(args) -> None:
    if not len(args) == 2:
        print("Usage:\n> python modify.py [article filename]")
        sys.exit()

# Makes sure the file name is actually a file
def check_file_valid(filename:str) -> None:
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist.")
        sys.exit()
