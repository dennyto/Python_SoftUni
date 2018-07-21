budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent = 0.3
        place = "Camp"
    elif season == "winter":
        spent = 0.7
        place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent = 0.4
        place = "Camp"
    elif season == "winter":
        spent = 0.8
        place = "Hotel"
elif budget > 1000:
    destination = "Europe"
    spent = 0.9

money_spent = "{0:.2f}".format(budget*spent)
print("Somewhere in " + destination)
print(place + " - " + str(money_spent))

