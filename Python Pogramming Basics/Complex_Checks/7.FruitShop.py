fruit = input()
day = input()
quantity = float(input())
result = "Error"

if day == "Monday" or  day == "Tuesday" or day == "Wednesday" or  day == "Thursday" or  day == "Friday":
    if fruit == "banana":
        result = 2.5 * quantity
    elif fruit == "apple":
        result = 1.2 * quantity
    elif fruit == "orange":
        result = 0.85 * quantity
    elif fruit == "grapefruit":
        result = 1.45 * quantity
    elif fruit == "kiwi":
        result = 2.7 * quantity
    elif fruit == "pineapple":
        result = 5.5 * quantity
    elif fruit == "grapes":
        result = 3.85 * quantity
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        result = 2.7 * quantity
    elif fruit == "apple":
        result = 1.25 * quantity
    elif fruit == "orange":
        result = 0.90 * quantity
    elif fruit == "grapefruit":
        result = 1.60 * quantity
    elif fruit == "kiwi":
        result = 3 * quantity
    elif fruit == "pineapple":
        result = 5.6 * quantity
    elif fruit == "grapes":
        result = 4.2 * quantity

if result != "Error":
    result = "{0:.2f}".format(result)

print(result)
