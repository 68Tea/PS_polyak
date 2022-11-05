import inspect
import sys
import requests
import random
data = "string"

def data2():
    pass

data = data2
print(inspect.ismodule(data2))
print(inspect.isclass(data2))5.
print(inspect.isfunction(data2))
print(sys.executable)
for met in dir(random):
    print(met)
