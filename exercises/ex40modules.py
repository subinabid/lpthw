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

class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing(self):
        print(self.lyrics)


happy_birthday = Song(["Happy birthday to you"])
bulls = Song(["Bulls song"])

happy_birthday.sing()
bulls.sing()