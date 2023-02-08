# Wordle clone
import sys
from random import choice
from rich.console import Console
from rich.style import Style

console = Console()
__style_0 = Style.parse("bold white")
__style_1 = Style.parse("bold white on yellow")
__style_2 = Style.parse("bold white on green")

__file = open("words.txt", "r")
__words = __file.read().splitlines()
__file.close()
__wordOfTheDay = choice(__words)

def main():
    console.clear()
    attempt = 0
    entries = []
    checks = []

    while attempt < 5:
        entry = input("Enter a 5 letter word: ").lower()
        
        if is_valid_entry(entry):
            attempt += 1
            entries.append(list(entry))
            check = check_word(entry, __wordOfTheDay)
            checks.append(check)

            console.clear()
            for i in range(attempt):
                print("\t", end = "")
                for l, s in  list(zip(entries[i], checks[i])):
                    if s == 2: printStyle = __style_2
                    elif s ==1:  printStyle = __style_1
                    else: printStyle = __style_0
                    console.print(l.upper(), style = printStyle, end = " ")
                print()

            if sum(check) == 10:
                sys.exit("\nCongrats! You got the right one")

        else:
            print("Check the word again")
    print("\n" + __wordOfTheDay)
    sys.exit("\nTry again")

def is_valid_entry(string):
    """Check if the entry is a valid 5 letter word"""
    return string in __words


def check_word(string, wordOfTheDay):
    """
    Analyze the input word
    Returns an array 
    2 - Letter is in the right position
    1 - Letter is contained in the word
    0 - Letter is not in the word"""
    word = list(string)
    wotd = list(wordOfTheDay)
    result = []

    for index, i in enumerate(word):
        if i == wotd[index]: result.append(2)
        elif i in wotd: result.append(1)
        else: result.append(0)
    
    return result


if __name__ == "__main__":
    main()