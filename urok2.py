class Student:
    print("Hi!")
    def __init__(self, height=160):
        self.height = height
        print("Im alive !")

first_ek = Student()
print(first_ek.height)

dima = Student(height=187)
print(dima.height)

