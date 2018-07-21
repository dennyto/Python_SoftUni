import math
loze = int(input())
grozde = float(input())
minLitters = int(input())
workers = int(input())

loze = loze * 0.4
totalGrozde = loze * grozde
totalLitters = totalGrozde / 2.5

if totalLitters >= minLitters:
    left = totalLitters - minLitters
    share = left / workers
    print("Good harvest this year! Total wine: " + str(math.floor(totalLitters)) + " liters.")
    print(str(math.ceil(left)) + " liters left -> " + str(math.ceil(share)) + " liters per person.")
else:
    left = minLitters - totalLitters
    print("It will be a tough winter! More " + str(math.floor(left)) + " liters wine needed.")
