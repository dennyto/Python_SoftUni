days = float(input())
wage = float(input())
rate = float(input())

monthly = days * wage
yearly = monthly * 12 + monthly * 2.5
tax = yearly * 0.25
finalYearly = yearly - tax
finalDaily = finalYearly/365*rate
print("{0:.2f}".format(finalDaily))

