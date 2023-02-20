# Learnings
1. ```item for item in list``` is called list comprehension. Eg ```sum_of_number_array = sum(n for n in numbers)``` 
1. ```*array``` is called a spread operator. The equivalent in javascript is  a ```...array```
1. Donot use hyphens ( - ) in filenames. Python scripts with hyphen in the file name cannot be imported as modules in the direct ```import modulename``` approach

## Notes

### argparse
handle agrs from the cli

### yield
Alternative to ```return()```
used in generators
returns one iten at a time from a generator
use ```next()``` to extract information


### dict

use dict.get() to get data from a dict if it is not sure if the item exists
eg:
dict  = {
    'a': 'apple',
    'b': 'ball',
    'c': 'cat;
}

```dict['a']``` and ```dict.get('a')``` will both return ```apple```
```dict['d']``` wil return an error while
```dict.get('d')``` will return ```None```

## To read
1. next


## Further reading
abstraction
indirection 
collections
collections.orderedDict