# Exercise 1
# Class for the bus

class Bus:
    def __init__(self, num_seats, color, driver):
        self.num_seats = num_seats
        self.color = color
        self.driver = driver
        self.num_bus_created = 0

    def increment_bus_created(self):
        self.num_bus_created += 1 

    def color_change1(self, color):
        self.color = color
