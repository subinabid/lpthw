from collections import defaultdict

def topk(filename):

    with open(filename) as file:
        words = file.read().split(" ")

    counts = defaultdict(lambda : 0)
    for word in words:
        counts[word] += 1

    temp = sorted([ (v,k) for (k,v) in counts.items() if k != ""], reverse=True)
    return (temp[0:5])

# Read
# Hash functions
# Reversible functions