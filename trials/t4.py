In [21]: l1 = [1,2,3,4, 5]

In [22]: l2 = [5,7,9]

In [23]: def odds(n): return bool(n % 2)

In [24]: odds(1)
Out[24]: True

In [25]: odds(2)
Out[25]: False

In [26]: map(odds, l1)
Out[26]: <map at 0x7f82f83dd340>

In [27]: list(map(odds, l1))
Out[27]: [True, False, True, False, True]

In [28]: list(map(odds, l2))
Out[28]: [True, True, True]

In [29]: filter(map(odds, l2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[29], line 1
----> 1 filter(map(odds, l2))

TypeError: filter expected 2 arguments, got 1

In [30]: filter(odds, l2)
Out[30]: <filter at 0x7f82f2f69a90>

In [31]: len(filter(odds, l1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[31], line 1
----> 1 len(filter(odds, l1))

TypeError: object of type 'filter' has no len()

In [32]: list(filter(odds, l2))
Out[32]: [5, 7, 9]

In [33]: len(list(filter(odds, l2)))
Out[33]: 3

In [34]: len(l2)  == len(list(filter(odds, l2)))
Out[34]: True

In [35]: len(l1)  == len(list(filter(odds, l1)))
Out[35]: False

