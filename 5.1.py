try:
    print("Start")
    print(10/0)
    print("End. No error")
except NameError:
    print("Houston, we have a problem!")
except ZeroDivisionError:
    print("ты двоечник учи математику лох")
print("End code")