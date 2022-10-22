class Human:
    def __init__(self, name="Human "):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def addpassenger(self, human):
        self.passenger.append(human)

    def print_passengers_names(self):
        if self.passenger!= []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passenger:
                    print(passenger.name)
            else:
                print(f"No passenger in {self.brand}")
hum1 = Human("Jack")
hum2 = Human("Lis")

auto1 = Auto("Mers")
auto2 = Auto("Tavria")

auto1.print_name_passenger()
auto2.print_name_passenger()

auto1.addpasanger(hum1)
auto1.addpasanger(hum2)

auto1.print_name_passenger()
auto2.print_name_passenger()

