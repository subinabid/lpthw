types_of_people = 10
x = f"There are {types_of_people} types of people"
print(x)

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Is it funny? {}"
print(joke_evaluation.format(hilarious))


hilarious = False
retry = True 
joke_evaluation = "Is it funny? {} {} "
print(joke_evaluation.format(hilarious, retry))

l = "left"
r = "right"
print(l + r)
print (l,r) # This operator adds a space between the 2 strings