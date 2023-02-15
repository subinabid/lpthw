# Custom functions on Stack and Queue
# Implement push() pop() for stack
# Implement a enque() and deque() for queue
# Tests

def push(l, i):
    l = l.__add__([i])
    return l, si

def pop(l):
    if len(l) > 0:
        i = l[len(l) -1]
        l.__delitem__(len(l)-1)
        return l, i
    else:
        print("Cannot operate on empty stack")

def enque(l, i):
    j = len(l)
    l = l.__add__([l[-1]])
    for k in reversed(range(j)):
        l[k] = l[k-1]
    l[0] = i
    return l

def deque(l):
    if len(l) > 0:
        i = l[0]
        del l[0]
        return l, i
    else:
        print("Cannot operate on an empty queue")

# Notes
# del() deletes an item. Eg del a[4] deletes index 4 element from a list
# __add__ adds a list of itmes to the list. Parameter should be a list, not string | usage a = a.__add__(["n", "m"])
# __contains__ check if an element exists in the list
# __delitem__ deletes an item from a list
# __getitem__ get an item from the list with an index ~or slice ?~ eg a.__getitem__(1) == a[1]
# __len__ get length of the list
# __sizeof__  get the size of the list in bytes
# __setitem__ set an item with index. similar to a[2] = "mango"