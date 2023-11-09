class Vehicle:
    def __init__(self):
        pass


class Car(Vehicle):
    def __init__(self):
        super().__init__()


class Plane(Vehicle):
    def __init__(self):
        pass


class Boat(Vehicle):
    def __init__(self):
        pass


class RaceCar(Car):
    def __init__(self):
        pass


# Testing
v = Vehicle()

c = Car()

p = Plane()

b = Boat()

rc = RaceCar()
