cars=100
space_in_a_car=20
space_in_car=40
drivers=30
passenger=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
averge_passengers_per_car=passenger/cars_driven

print "there are", cars, "cars avaible"
print "there are only", drivers, "drivers avaible"
print "there will be", cars_not_driven, "empty cars today"
print "we can trasnport", carpool_capacity, "people today"
print "we have", passenger, "to parpool today"
print "we need to put about", averge_passengers_per_car, "in each car"
