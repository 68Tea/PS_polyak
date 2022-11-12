class Mum:
    height = 160
    eyes = "Blue"
    hair_color = "Black"
    ability = "flexibility"

class Dad:
    height = 170
    eyes = "Green"
    peculiarities = "Big eyes"
    hair_color = "Yellow"


class Son(Dad, Mum):
    pass

Jack = Son()

print(f"Height: {Jack.height}")
print(f"Eyes: {Jack.eyes}")
print(f"Ability: {Jack.ability}")
print(f"Peculiarities: {Jack.peculiarities}")
print(f"Hair_color: {Jack.hair_color}")