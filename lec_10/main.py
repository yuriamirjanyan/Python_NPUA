from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self):
        super().__init__()


class Plane(Vehicle):
    def __init__(self):
        super().__init__()


class Boat(Vehicle):
    def __init__(self):
        super().__init__()


class RaceCar(Car):
    def __init__(self):
        super().__init__()


# Testing
v = Vehicle()

c = Car()

p = Plane()

b = Boat()

rc = RaceCar()

