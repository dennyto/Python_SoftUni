import math
vhod = input()
side = float(input())
if vhod == "square":
     lice = side * side
elif vhod == "rectangle":
     width = float(input())
     lice = side * width
elif vhod == "circle":
     lice = side*side*math.pi
elif vhod == "triangle":
     height = float(input())
     lice = (side * height) / 2

print("{0:.3f}".format(lice))




