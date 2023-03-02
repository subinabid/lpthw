class Stack():

    def __init__(self):
        self.item = []

    def push(self, i):
        self.item.append(i)
        return self
    
    def pop(self):
        try:
            k = self.item[-1]
            del self.item[-1]
            return k
        except IndexError:
            return None

    # Only for testing       
    def to_list(self):
        return self.l
    
class Q():

    def __init__(self):
        self.l = []

    def enque(self, i):
        self.l.append(i)
        return self

    def deque(self):
        try:
            i = self.l[0]
            del self.l[0]
            return i  
        except IndexError:
            raise QEmpty()
        
    # Only for testing       
    def to_list(self):
        return self.l

class QEmpty(Exception):
    pass

class StackEmpty(Exception):
    pass


