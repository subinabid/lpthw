# Wordle clone
import sys
from random import choice
from rich.console import Console

console = Console()

def main():

    wordOfTheDay = pick_wotd()
    attempt = 0
    entries = []
    checks = []
    styles = []


    while attempt < 5:
        entry = input("Enter a word: ").upper()
        
        if is_valid_entry(entry):
            attempt += 1
            entries.append(entry)
            check, style = check_word(entry, wordOfTheDay)
            checks.append(check)
            styles.append(style)

            for count, word in enumerate(entries):
                console.print(word[0], style = styles[count][0], end="")
                console.print(word[1], style = styles[count][1], end="")
                console.print(word[2], style = styles[count][2], end="")
                console.print(word[3], style = styles[count][3], end="")
                console.print(word[4], style = styles[count][4])

            if sum(check) == 5:
                sys.exit("\nCongrats")

        else:
            print("Enter a 5 letter Word")


def is_valid_entry(string):

    test_length = True if len(string) == 5 else False
    test_chars = string.isalpha()

    return True if test_length and test_chars else False

def check_word(string, wordOfTheDay):
    word = list(string)
    ref_word = list(wordOfTheDay)
    result = []
    style = []

    for index, i in enumerate(word):
        if i == ref_word[index]:
            result.append(1)
            style.append("bold white on green")
        elif i in ref_word:
            result.append(0)
            style.append("bold white on yellow")
        else:
            result.append(0)
            style.append("bold white")
    
    return result, style

def pick_wotd():
    file = open("words.txt", "r")
    words = file.read().splitlines()
    file.close()

    return choice(words).upper()

if __name__ == "__main__":
    main()