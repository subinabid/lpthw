hairs = ['black', 'brown', 'blonde', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'grapes']
change = [1, 'pennies', 2 , 'dimes', 3 , 'qtr']

for number in the_count:
    print(f"The number is {number}")

print("Sum is:", sum(n for n in the_count))

elements = []
elements.extend([*range(1,21)])

print(elements)
for i in elements:
    print (i)
