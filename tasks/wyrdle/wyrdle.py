# Wordle clone
import sys
from random import choice
from rich.console import Console
from rich.style import Style
import itertools

console = Console()
style_0 = Style.parse("bold white")
style_1 = Style.parse("bold white on red")
style_2 = Style.parse("bold white on yellow")
style_3 = Style.parse("bold white on green")

with open("words.txt", "r") as f:
    words = f.read().splitlines()
    __wordOfTheDay = choice(words)

alphabets = list("abcdefghijklmnopqrstuvwxyz")
alphabets_status = list(itertools.repeat(0, 26))

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
                    if s == 3: printStyle = style_3
                    elif s ==2:  printStyle = style_2
                    else: printStyle = style_0
                    console.print(l.upper(), style = printStyle, end = " ")
                print("")
            
            print()   
            for a, s in list(zip(alphabets, alphabets_status)):
                if s == 3: printStyle = style_3
                elif s ==2:  printStyle = style_2
                elif s ==1: printStyle = style_1
                else: printStyle = style_0
                console.print(a.upper(), style = printStyle, end = " ")
            print("\n\n")

            if sum(check) == 15:
                sys.exit("\nCongrats! You got the right one")

        else:
            print("Check the word again")

    console.print(__wordOfTheDay.upper(), style = style_3)
    sys.exit("\nBetter luck next time")


def is_valid_entry(string):
    """Check if the entry is a valid 5 letter word"""
    return string in words


def check_word(string, wordOfTheDay):
    """Analyze the input word and returns an array of status 
    2 - Letter is in the right position
    1 - Letter is contained in the word
    0 - Letter is not in the word"""
    word = list(string)
    wotd = list(wordOfTheDay)
    result = []

    for index, i in enumerate(word):
        if i == wotd[index]: 
            result.append(3)
            update_alphabet(i, 3)
        elif i in wotd: 
            result.append(2)
            update_alphabet(i, 2)
        else: 
            result.append(1)
            update_alphabet(i, 1)
    
    return result


def update_alphabet(alphabet, status):
    """Update the status of each alphabet"""
    n = alphabets.index(alphabet)
    alphabets_status[n] = status if alphabets_status[n] <status else alphabets_status[n]


if __name__ == "__main__":
    main()