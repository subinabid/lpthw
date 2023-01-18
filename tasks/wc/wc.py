# Module to replicate wc command in Linux
# Returns the number of lines, words, and characters of a file(s)

import sys

def wc(filename):
    """ Return the number of lines, words and characters"""
    with open(filename) as f:
        lines = f.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

    return line_count, word_count, char_count, filename

def wctotal(filenames):
    """ Return the total number of lines, words and characters for multiple files"""
    line_count = word_count = char_count = 0
    info = []
    for filename in filenames:
        i, j, k, l = wc(filename)
        info.append((i,j,k,l))
        line_count += i
        word_count += j
        char_count += k 
    if len(filenames) > 1:
        info.append((line_count, word_count, char_count, "Total"))
    
    return info

if __name__ == "__main__":

    try:
        if len(sys.argv) < 2:
            #sys.exit("Error: Need a file as argument")
            raise IndexError

        info = wctotal(sys.argv[1:])
        for a, b, c, d in info:
            print(f"{a} \t{b} \t{c} \t\t{d}")

    except IndexError:
        sys.exit("Error: Need a file as argument")
    
    except FileNotFoundError as e:
        sys.exit(f"Error: File {e.filename} is not found")

    except IsADirectoryError as e:
        sys.exit(f"Error: Argument {e.filename} is a directory")

    except UnicodeDecodeError:
        sys.exit(f"Error: One of the files is not a supported format")
        # File name is nt available in the errormessage
        # Error happens during read()