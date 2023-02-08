l1 = [1, 2, 3, 4]
l2 = ['a', 's', 'd', 'f']
l3 = [15, 12, 32, 46, 67]
l4 = [15, 26, 37, 48]

l1.extend(l2)
l1.extend(l3)

# for i in l1:
#     print (i)

# for j in range(min(len(l3), len(l4))):
#     print (l3[j], l4[j])

ll = zip(l3, l4)
for k in ll:
    print(k)