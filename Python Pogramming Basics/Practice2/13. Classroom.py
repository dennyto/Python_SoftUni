h = float(input())
w = float(input())

h = h*100
w = w*100 - 100

seats = (h//120) * (w//70) - 3
print(int(seats))


