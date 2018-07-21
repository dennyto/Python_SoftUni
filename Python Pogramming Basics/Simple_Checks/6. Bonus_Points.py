num = int(input())

if num <= 100:
    bonus = 5
elif 100 < num <= 1000:
    bonus = num * 0.2
elif num > 1000:
    bonus = num * 0.1

if num % 2 == 0:
    bonus = bonus + 1
elif num % 10 == 5:
    bonus = bonus + 2

finalNum = num + bonus
print(bonus)
print(finalNum)
