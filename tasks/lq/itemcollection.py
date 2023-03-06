class Stack:
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
        return self.item


class Q:
    def __init__(self):
        self.item = []

    def enque(self, i):
        self.item.append(i)
        return self

    def deque(self):
        try:
            i = self.item[0]
            del self.item[0]
            return i
        except IndexError:
            raise QEmpty()

    # Only for testing
    def to_list(self):
        return self.item


class FileStack:
    def __init__(self):
        self.filename = "test.txt"

    def push(self, i):
        with open("test.txt", "a") as f:
            f.write(str(i) + "\n")
            return self


class QEmpty(Exception):
    pass


class StackEmpty(Exception):
    pass
