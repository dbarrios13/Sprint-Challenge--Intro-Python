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

# Base of the type of Vehicle
# class Vehicle:     
#     def __init__(self, type_of):
#         self.type_of = type_of

#     def __str__(self):
#         return f'Type of vehicle: {self.type_of}'


# # Base of Flight Vechiles.... base for airplane and starship
# class FlightVehicle(Vehicle): 
#     def __init__(self, name, type_of):
#         super().__init__(type_of)
#         self.name = name

#     def __str__(self):
#         return f'{self.name} is a {self.type} of vehicle'

# class Airplane(FlightVehicle):
#     def __init__(self, name, type_of, model):
#         super().__init__(name, type_of)
#         self.model = model

# class Starship(FlightVehicle):
#     def __init__(self, name, type_of, model, galaxy):
#         super().__init__(name, type_of)
#         self.model = model
#         self.galaxy = galaxy



# # Base for ground vehicles.... base for car and motorcycle
# class GroundVehicle(Vehicle):
#     def __init__(self, name, type_of):
#         super().__init__(type_of)
#         self.name = name

# class Car(GroundVehicle):
#     def __init__(self, name, type_of, make, model, year):
#         super().__init__(name, type_of)
#         self.make = make
#         self.model = model
#         self.year = year

# class Motorcycle(GroundVehicle):
#     def __init__(self, name, type_of, make, model):
#         super().__init__(name, type_of)
#         self.make = make
#         self.model = model




# Base of the type of Vehicle
class Vehicle:
    pass 

# Base of Flight Vechiles.... base for airplane and starship
class FlightVehicle(Vehicle): 
    pass 

class Airplane(FlightVehicle):
    pass 

class Starship(FlightVehicle):
    pass 


# Base for ground vehicles.... base for car and motorcycle
class GroundVehicle(Vehicle):
    pass 

class Car(GroundVehicle):
    pass 

class Motorcycle(GroundVehicle):
    pass 