import math
hrs = int(input())
days = int(input())
workers = int(input())

extraHrs = workers * days * 2
days = days * 0.9
hrsWorked = days * 8
totalHrs = math.floor(hrsWorked + extraHrs)

if hrs > totalHrs:
    print("Not enough time!" + str(hrs - totalHrs) + " hours needed.")
else:
    print("Yes!" + str(totalHrs - hrs) + " hours left.")

