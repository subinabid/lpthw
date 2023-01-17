name = 'Subin'
age = 35 
height = 180
weight = 84
eyes = 'Black'
teeth = 'White'
hair = 'Black'
bmi = round(weight / (height/100) / (height/100),2)

print(f"Name - {name}")
print(f"Age - {age}")
print(f"Height - {height}cms and weight - {weight} kgs")
print(f"BMI { bmi }")

x = ("apple", "banana", "cherry")
print( "a", "b", sep = "---")
print( "a", "b", sep = "---", end = "|")
print()
print( "a", "b", sep = "---", end = "")