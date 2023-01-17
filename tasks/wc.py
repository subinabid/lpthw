# Module to replicate wc command in Linux
# Returns the number of lines, words, and characters of a file(s)

import os
import sys

def wc(filename):
    """ Return the number of lines, words and characters"""
    with open(filename) as f:
        lines = f.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

    return line_count, word_count, char_count

def wct(filenames):
    """ Return the total number of lines, words and characters for multiple files"""
    line_count = word_count = char_count = 0
    for filename in filenames:
        line_count += wc(filename)[0]
        word_count += wc(filename)[1]
        char_count += wc(filename)[2] 
    
    return line_count, word_count, char_count

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Error! File(s) argument missing")

    elif len(sys.argv) > 1:

        filelist = []
        for filename in sys.argv[1:]:
            if os.path.isfile(filename):
                filelist.append(filename)

        if len(filelist) == 0:
            print(f"Error! File(s) is not found")
        
        else:

            if len(filelist) != len(sys.argv[1:]):
                print("One of the input(s) was not a valid file")

            for filename in filelist:
                try:
                    line_count, word_count, char_count = wc(filename)
                    print(f"{line_count} \t{word_count} \t{char_count} \t\t{filename}")

                except UnicodeDecodeError:
                    print(f"Error! {filename} is an unsupported filetype")

            if len(filelist) > 1:
                line_count_total, word_count_total, char_count_total = wct(filelist) 
                print(f"{line_count_total} \t{word_count_total} \t{char_count_total} \t\tTotal")