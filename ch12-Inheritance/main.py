
# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.
# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.


class Vehicle:

        def __init__(self, type, make, model, hp, torque):
            self.type = type
            self.make = make
            self.model = model
            self.horsepower = hp
            self.torque = torque

        def drive(self, color):
            print(f'The {color} car is really fast')

        def turn(self, direction):
            print(f'The car has turned {direction}')

        def stop(self):
            print(f'The car has come to a stop')

class Skyline(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "coupe", "Nissan", "Skyline", 276, 289)

class Z(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "coupe", "Nissan", "280z", 170, 163)

class Mustang(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "coupe", "Ford" "Mustang", 210, 180)

class Cuda(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "coupe", "Plymouth", "Hemi Cuda", 245, 230)

class Supra(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "coupe", "Toyota", "Supra", 289, 267)


wow = Skyline()
wow.drive("blue")
wow.turn("left")
wow.stop()