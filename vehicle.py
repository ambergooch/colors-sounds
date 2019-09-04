class Vehicle:
    def __init__(self):
        self.model = ""
        self.main_color = ""
        self.maximum_occupancy = ""

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
        print(f"This vehicle turned {direction}")

    def stop(self):
        print("This vehicle stopped.")

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        self.battery_kwh = "100%"

    def drive(self):
        print(f"The {self.main_color} {self.model} drives past. Zoooom!")

    def turn(self, direction):
        print(f"The {self.model} turned {direction}")

    def stop(self):
        print(f"The {self.main_color} Tesla rolls to a stop after rolling a mile down the road.")

class Nissan(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        self.battery_kwh = "100%"

    def drive(self):
        print(f"The {self.main_color} {self.model} drives past.Rhoooom!")

    def turn(self, direction):
        print(f"The {self.model} turned {direction}")

    def stop(self):
        print("This vehicle stopped.")

class Chevy(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        self.fuel_capacity = "100%"

    def drive(self):
        print(f"The {self.main_color} {self.model} drives past. Froooom!")

    def turn(self, direction):
        print(f"The {self.model} turned {direction}")

    def stop(self):
        print(f"The {self.main_color} {self.model} slowly rolled to a stop.")

class Ford(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        self.fuel_capacity = "100%"

    def drive(self):
        print(f"The {self.main_color} {self.model} drives past. Vroooom!")

    def turn(self, direction):
        print(f"The {self.model} turned {direction}")

    def stop(self):
        print("This vehicle stopped.")

class Dodge(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        self.fuel_capacity = "100%"

    def drive(self):
        print(f"The {self.main_color} {self.model} drives past. Meow!")

    def turn(self, direction):
        print(f"The {self.model} turned {direction}")

    def stop(self):
        print(f"The {self.model} screeched to a halt.")

modelS = Tesla()
gtr = Nissan()
corvette = Chevy()
mustang = Ford()
charger = Dodge()

modelS.model = "Model S"
gtr.model = "GT-R"
corvette.model = "Corvette"
mustang.model = "Mustang"
charger.model = "Charger"

modelS.main_color = "black"
gtr.main_color = "white"
corvette.main_color = "red"
mustang.main_color = "silver"
charger.main_color = "yellow"

modelS.maximum_occupancy = 2
gtr.maximum_occupancy = 4
corvette.maximum_occupancy = 2
mustang.maximum_occupancy = 4
charger.maximum_occupancy = 4

modelS.drive()
gtr.drive()
corvette.drive()
mustang.drive()
charger.drive()

modelS.turn("left")
gtr.turn("right")
corvette.turn("left")
mustang.turn("right")
charger.turn("left")

modelS.stop()
gtr.stop()
corvette.stop()
mustang.stop()
charger.stop()