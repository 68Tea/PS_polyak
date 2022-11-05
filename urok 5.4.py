def checker(var1):
    if type(var1) != str:
        raise TypeError(f"Sorry, we can't work with {var1}, we need class str")
    else:
        return var1


var_check = 12
checker(var_check)