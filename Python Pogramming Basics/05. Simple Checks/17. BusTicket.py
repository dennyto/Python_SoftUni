n = int(input())
time = input()

if n < 20:
    if time == "day":
        price = n * 0.79 + 0.7
    else:
        price = n * 0.9 + 0.7
elif n < 100:
    price = n * 0.09
else:
    price = n * 0.06

print(price)
