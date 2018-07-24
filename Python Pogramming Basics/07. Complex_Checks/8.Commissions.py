city = input()
sales = float(input())
commission = "error"
percent = 0

if 0 <= sales <= 500:
    if city == "Sofia":
        percent = 0.05
    elif city == "Varna":
        percent = 0.045
    elif city == "Plovdiv":
        percent = 0.055
elif 500 < sales <= 1000:
    if city == "Sofia":
        percent = 0.07
    elif city == "Varna":
        percent = 0.075
    elif city == "Plovdiv":
        percent = 0.08
elif 1000 < sales <= 10000:
    if city == "Sofia":
        percent = 0.08
    elif city == "Varna":
        percent = 0.1
    elif city == "Plovdiv":
        percent = 0.12
elif sales > 10000:
    if city == "Sofia":
        percent = 0.12
    elif city == "Varna":
        percent = 0.13
    elif city == "Plovdiv":
        percent = 0.145

if percent != 0:
    commission = percent * sales

print(commission)
