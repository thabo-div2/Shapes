class Shapes:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def area(self):
        print("I am a :" + self.name + "\n" +
              "I have " + self.sides + "sides")


class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        return result


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14 * (self.radius**2)
        return result


class Triangle(Shapes):
    def __init__(self, base, height):
        self.height = height
        self.base = base

    def area(self):
        result = (1/2*self.base) * self.height
        return result



