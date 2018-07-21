num = float(input())
original = input()
toUnit = input()


if original == "mm":
    num = num / 1000
elif original == "cm":
    num = num / 100
elif original == "mi":
    num = num / 0.000621371192
elif original == "in":
    num = num / 39.3700787
elif original == "km":
    num = num / 0.001
elif original == "ft":
    num = num / 3.2808399
elif original == "yd":
    num = num / 1.0936133
elif original == "m":
    num = num

if toUnit == "mm":
    final = num * 1000
elif toUnit == "cm":
    final = num * 100
elif toUnit == "mi":
    final = num * 0.000621371192
elif toUnit == "in":
    final = num * 39.3700787
elif toUnit == "km":
    final = num * 0.001
elif toUnit == "ft":
    final = num * 3.2808399
elif toUnit == "yd":
    final = num * 1.0936133
elif toUnit == "m":
    final = num

print(final)


