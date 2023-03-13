def print_two(*args):
    arg1, arg2 = args
    print(f"Arg 1: {arg1} | Arg 2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"Arg 1: {arg1} | Arg 2: {arg2}")

print_two("Sub", "Abid")
print("Again")
print_two_again("Sub", "Abid")