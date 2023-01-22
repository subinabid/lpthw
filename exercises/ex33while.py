# i = 0
# numbers  = []

# while i <6 :
#     print(f"i = {i}")
#     numbers.append(i)
#     i +=1
#     print(f"Numbers are {numbers}")
#     print(f"i = {i}")

# print(f"Final numbers {numbers}")

# for n in numbers:
#     print(n)

import sys

def num_gen(number, increment = 1):
    i = 0
    numbers = []

    while i < number :
        numbers.append(i)
        i += increment
    return numbers

if __name__ == "__main__":
    print( num_gen(int(sys.argv[1]), int(sys.argv[2])))
