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
    info = [wc(filename) for filename in filenames]
    
    if len(info) > 1:
        line_count = sum(i[0] for i in info)
        word_count = sum(i[1] for i in info)
        char_count = sum(i[2] for i in info)
        info.append((line_count, word_count, char_count, "Total"))
    
    return info

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Error: Need a file as argument")

        info = wctotal(sys.argv[1:])    
        for a, b, c, d in info:
            print(f"{a} \t{b} \t{c} \t\t{d}")
    
    except FileNotFoundError as e:
        sys.exit(f"Error: File {e.filename} is not found")

    except IsADirectoryError as e:
        sys.exit(f"Error: Argument {e.filename} is a directory")

    except UnicodeDecodeError:
        sys.exit(f"Error: One of the files is not a supported format")


if __name__ == "__main__":
    main()