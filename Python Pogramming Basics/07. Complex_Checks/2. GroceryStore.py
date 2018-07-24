product = input().lower()
city = input().lower()
quantity = float(input())

if product == "coffee":
    if city == "sofia":
        price = 0.5 * quantity
    elif city == "plovdiv":
        price = 0.4 * quantity
    elif city == "varna":
        price = 0.45 * quantity
elif product == "water":
    if city == "sofia":
        price = 0.8 * quantity
    elif city == "plovdiv":
        price = 0.7 * quantity
    elif city == "varna":
        price = 0.7 * quantity
elif product == "beer":
    if city == "sofia":
        price = 1.2 * quantity
    elif city == "plovdiv":
        price = 1.15 * quantity
    elif city == "varna":
        price = 1.1 * quantity
elif product == "sweets":
    if city == "sofia":
        price = 1.45 * quantity
    elif city == "plovdiv":
        price = 1.3 * quantity
    elif city == "varna":
        price = 1.35 * quantity
elif product == "peanuts":
    if city == "sofia":
        price = 1.6 * quantity
    elif city == "plovdiv":
        price = 1.5 * quantity
    elif city == "varna":
        price = 1.55 * quantity

print(price)
