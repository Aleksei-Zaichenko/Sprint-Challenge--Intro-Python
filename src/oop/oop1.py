# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class for GroundVehicle and flightVehicle classes
class Vehicle:
    pass

# base class for Car and Motorcycle classes
class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# base class for Aiplane and Starship classes
class FlightVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass