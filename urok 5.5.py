class BuildingError(Exception):
    def __str__(self):
        return  f"With so much material the house cannot built!"

def check_material(material1, limit):
    if material1 >=  limit:
        print("Go! ")
    else:
        raise BuildingError()

material = 400
limit = 350

check_material(material, limits)