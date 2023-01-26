# Replicate Tree in Linux

import os
import argparse
from colorama import Fore

def tree(dir, level):
    """Yields the files and folders in the specified direcotry"""
    for i in os.scandir(dir):
        yield(i, level)


def main(path, depth, level = 1):
    for f, print_level in tree(path, level):
        prefix = "   " * (print_level - 1)  
        tail =  "-- " if print_level == 1 else " |-- "  
        
        if f.is_dir():
            print ("|" + prefix + tail + Fore.BLUE + f.name + Fore.RESET)
            if print_level < depth:
                main(f.path, depth, level + 1)

        elif f.is_file():
            print ("|" + prefix + tail + f.name )
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "Tree utility")
    parser.add_argument("-p","--path", default = ".", help = "Location")
    parser.add_argument("-d", "--depth", default = 1, type=int, help="Levels of sub directories")
    args = parser.parse_args()

    print(".")
    main(args.path, args.depth)