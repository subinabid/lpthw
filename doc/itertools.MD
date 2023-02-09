# itertools

## Infinite Iterators
- count()
- cycle()
- repeat()

## Iterators termminating on the shortest input sequence
- accumulate()
- chain()


## Combined iterators
Iterator |Arguments |Results |
---|---|---|
product()| p, q, … [repeat=1] | cartesian product, equivalent to a nested for-loop
permutations()| p[, r] |r-length tuples, all possible orderings, no repeated elements
combinations()|p, r|r-length tuples, in sorted order, no repeated elements
combinations_with_replacement() |p, r |r-length tuples, in sorted order, with repeated elements