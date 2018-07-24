month = input()
hours = float(input())
people = int(input())
day_or_night = str.lower(input())

price = 0

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price = 10.5
    else:
        price = 8.4
else:
    if day_or_night == "day":
        price = 12.6
    else:
        price = 10.2

