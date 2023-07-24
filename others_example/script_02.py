import script_01
from script_01 import y

# import py file from other script and use it here
a = "Hii"
print(script_01.x, a, y)
# return all name inside the module by calling dir() function
print(dir(script_01))
