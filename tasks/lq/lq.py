# Custom functions on Stack and Queue
# Implement push() pop() for stack. Stack operaties on right end
# Implement enque() and deque() for queue. Queue operates on left end

def push(l, i):
    l.append(i)
    return l

def pop(l):
    try:
        k = l[-1]
        del l[-1]
        return k
    except IndexError:
        return None

def enque(l, i):
    j = len(l)
    
    if j == 0:
        return push(l,i)

    else:
        l.append(l[-1])
        while j > 1:
            l[j-1] = l[j-2]
            j -= 1
        l[0] = i
        return l

def deque(l):
    try:
        i = l[0]
        del l[0]
        return i  
    except IndexError:
        return None

# Sajid's code. Isnt this the same as push?
def enqueue(queue, item):
    queue.append(item)
    return queue

# Sajid's code
def dequeue(queue):
    return queue.pop(0)

# Notes
# del() deletes an item. 
# Eg del a[4] deletes index 4 element from a list
# Eg: del a deletes variabl a

# Example of private functions
class A():
     
    def __init__(self, n) -> None:
        self.n = n
    
    def __add__(self, other):
        return A(self.n + other.n)