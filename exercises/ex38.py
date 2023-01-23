sentence = "This is a short sentence"
stuff = sentence.split(" ")
more_stuff = "some random sentence that i made up to fill space one two three".split(" ")

print(stuff)
print(more_stuff)

while len(stuff) < 10:
    stuff.append(more_stuff.pop(2))


print(f"Stuff : {stuff}")
print(f"More Stuff : {more_stuff}")

print("Cool Stuffs!!")
print(stuff[0])
print(stuff[-1])
print(stuff.pop())
print(stuff.pop())
print(stuff.pop())
print(stuff.pop())

print(' '.join(stuff))
print('#'.join(stuff[2:5]))