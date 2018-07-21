showing = input()
rows = int(input())
columns = int(input())
seats = rows * columns

if showing == "Premiere":
    sales = seats * 12
elif showing == "Normal":
    sales = seats * 7.5
elif showing == "Discount":
    sales = seats * 5

print("{0:.2f} leva".format(sales))
