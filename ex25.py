def break_words(stuff):
    """Break up words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the forst word after popping"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """prints last wword after popping it """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """returns a sorted sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the forst and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Prints the forst and last words of a sentence after sorting"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
