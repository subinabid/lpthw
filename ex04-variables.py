cars = 100
seat = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * seat
passenger_per_car = carpool_capacity / cars_driven

print ("There are",cars, "cars available")