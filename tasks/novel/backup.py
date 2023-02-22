
file = open('/usr/share/dict/README')
word_list = file.read().split(" ")
counts = {}

for i in word_list:
    if i in counts.keys():
        counts[i] += 1
    else:
        counts[1] = 1

print(counts) 




