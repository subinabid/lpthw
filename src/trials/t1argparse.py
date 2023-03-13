import argparse
parser = argparse.ArgumentParser(description= "what this file does")

# parser.add_argument("echo", help = "echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

# parser.add_argument("square", help = "Prints the square of the given number", type = int)
# args = parser.parse_args()
# print(args.square ** 2)

# parser.add_argument("square", type= int, 
#     help= "Prints the square of the number")
# parser.add_argument("-v", "--verbosity", type= int, choices= [1, 2],
#     help= "increase output verbosity",)
# args = parser.parse_args()
# answer = args.square ** 2

# if args.verbosity == 2:
#     print(f"Square of {args.square} is {answer}")

# elif args.verbosity == 1:
#     print(f"{args.square}^2 = {answer}")

# else:
#     print(answer)

# parser.add_argument("square", type= int, 
#     help= "Prints the square of the number")
# parser.add_argument("-v", "--verbosity", action= "count", default = 0,
#     help= "increase output verbosity",)
# args = parser.parse_args()
# answer = args.square ** 2

# if args.verbosity >= 2:
#     print(f"Square of {args.square} is {answer}")

# elif args.verbosity == 1:
#     print(f"{args.square}^2 = {answer}")

# else:
#     print(answer)

parser.add_argument("x", type = int, help = "Base")
parser.add_argument("y", type = int, help = "Exponent")
parser.add_argument("-v", "--verbosity", action = "count", default = 0, help = "Verbose Output")
args = parser.parse_args()
answer = args.x ** args.y

if args.verbosity >= 2:
    print(f"{args.x} to the power {args.y} is {answer}")


elif args.verbosity == 1:
    print(f"{args.x} ^ {args.y} = {answer}")


else:
    print(answer)