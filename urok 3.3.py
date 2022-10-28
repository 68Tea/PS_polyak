class Human:
    height = 170

class Student(Human):
    pass


class Worker(Human):
    pass

vasya = Student()
dima = Worker()
vika = Student()

print(vasya.height)
print(dima.height)
print(vika.height)
