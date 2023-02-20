import mystuff
mystuff.apple()
print(mystuff.orange)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "Some string"
    
    def apple(self):
        print("Classy Apples")

thing = MyStuff()
thing.apple()
print(thing.tangerine)