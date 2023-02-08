l1 = [1,2,3,4, 5]
l2 = [5,7,9]
def odds(n): return bool(n % 2)
len(l2)  == len(list(filter(odds, l2)))