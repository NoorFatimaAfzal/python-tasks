class cirle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class cylinder(cirle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return self.area() * self.height
    
