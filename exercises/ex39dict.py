# Mapping of States to Abbrevation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Set of States and Cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Another way of adding cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Printing
print('-' * 10 )
print("NY State has:", cities['NY'])
print("CA State has:", cities['CA'])

# Printing state info
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# Dict on dict
print("-" * 10)
print("Michigan has:", cities[states['Michigan']])
print("California has:", cities[states['California']])

# Print all states
print('-' * 10)
# print(states)
# print(states.items())
# print(list(states.items()))
# print(states['Oregon'])
# print(list(states.items())[1])
# a, b  = list(states.items())[1]
# print(a)
# print(b)

for state, abbrev in list(states.items()):
    print(f"State {state} is abbreviated as {abbrev}")

# Print all cities
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has city {city}")

# Print State & City combo
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"State {state} has the city {cities[abbrev]}")

# Other features
print('-' * 10)
print(states.get('New Yor'))
print(states.get('New Yor', "Does not Exist"))
# print(states['New Yor']) will give an error


# Notes
# Using dict.get() returns None if item is not found
# Direct access will throw an error if match is not found
# dict.keys() returns a list of keys
# dict.values() returns a list of values
# dict.items() returns an iterable of tuples
# dict.clear() clears the dict
# dict.pop(key) pops single item matching the key
# dict.popitem() pops the last item
# dict.fromkeys() creates a new dict based on keys and a value. IDK why this operated on a dict ????
