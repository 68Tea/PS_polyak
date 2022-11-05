try:
    try:
        print("Start")
        print(Hello)
        print("End. No error")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)