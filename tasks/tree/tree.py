# Replicate Tree in Linux
# Have an option to add Levels

import os
import sys
from colorama import Fore, Style

def tree(dir = '.'):
    """
    Get details of files and directories
    Optional input is a path
    if path is not provided, the pwd is used as default
    """
    return os.scandir(dir)


def print_tree(treeinfo, depth = 1, level = 1):
    """
    Prints the tree structure
    Required input is theoutput of the tree() function
    Optional input is the depth of iteration 
    """

    d = int(depth)
    l = int(level)
    
    if l == 1: 
        print(".")
    
    for i in treeinfo:
        print_tree_item(i, l)

        if i.is_dir() and d > 1: 
                print_tree(tree(i.path), d-1, l+1)


def print_tree_item(tree_item, level = 1):
    """
    Prints the item
    Formatting for Files and directories
    """

    if tree_item.is_dir(): 
        print("|-- " * level + Fore.BLUE + tree_item.name + Fore.RESET)
            

    elif tree_item.is_file(): 
        print("|-- " * level + tree_item.name)    

    
def main():
    try:
        inputs = sys.argv
        
        if len(inputs) == 1:
            print_tree(tree())
        
        elif len(inputs) == 2:
            print_tree(tree(sys.argv[1]))  

        elif len(inputs) == 3:
           print_tree(tree(sys.argv[1]), depth=sys.argv[2])  
        
        else:
            raise IndexError
            
    except IndexError:
        sys.exit("Error: Please check the inputs")

    except FileNotFoundError:
        sys.exit("Error: Directory is not found")

    # except TypeError as e:
    #     sys.exit(e)

if __name__ == "__main__":
    main()