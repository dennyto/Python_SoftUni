daffodils = int(input())
roses = int(input())
tulips = int(input())
season = str.lower(input())
holiday = str.lower(input())

if season == "spring" or season == "summer":
    total_daffodils = daffodils * 2
    total_roses = roses * 4.1
    total_tulips = tulips * 2.5
elif season == "fall" or season == "winter":
    total_daffodils = daffodils * 3.75
    total_roses = roses * 4.5
    total_tulips = tulips * 4.15

total_flowers = total_roses + total_tulips + total_daffodils

if holiday == "y":
    total_flowers = total_flowers * 1.15

if tulips > 7 and season == "spring":
    total_flowers = total_flowers * 0.95

if roses >= 10 and season == "winter":
    total_flowers = total_flowers * 0.9

if (daffodils + tulips + roses) > 20:
    total_flowers = total_flowers * 0.8

flowers = total_flowers + 2

print(f"{flowers:.2f}")





