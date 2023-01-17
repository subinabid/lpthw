formatter = " {} {} {} {} "

#print(formatter)
print(formatter.format(1,2,3,4))
#print(formatter.format(1,2,3,4,5,6))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(formatter.format(1,2,3,4),formatter.format(5,6,7,8),formatter,formatter))