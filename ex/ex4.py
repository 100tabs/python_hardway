cars = 100
space_in_cars = 4
drivers = 30
passangers = 90 
cars_not_driven = cars -  drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
avarage_passenger_per_car = passangers / cars

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passangers, "to carpool today.")
print("We ned to put about", avarage_passenger_per_car, "in each car.")