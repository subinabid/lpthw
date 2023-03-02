class Stack():

    def __init__(self, backend):
        self._backend = backend

        if backend == 'list':
            self._items = []
        else:
            self._items = open('/tmp/stack', 'w')


    # Push to the right
    def push(self, item):
        if self.backend == "list":
            self.items.append(item)
        else:
            self.items.write(str(item))
            self.items.flush()

        return self