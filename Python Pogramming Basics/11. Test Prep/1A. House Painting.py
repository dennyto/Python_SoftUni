x = float(input())
y = float(input())
h = float(input())

side_walls = 2* x * y - 2 * 1.5 * 1.5
front_walls = 2 * x * x - 1.2 * 2
roof_sides = 2 * x * y
roof_front = x * h

green = (side_walls + front_walls) / 3.4
red = (roof_front + roof_sides) / 4.3

print('{:.2f}'.format(green))
print('{:.2f}'.format(red))
