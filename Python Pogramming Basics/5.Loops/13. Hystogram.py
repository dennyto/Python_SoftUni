n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range (0, n):
    a = int(input())
    if a >= 800:
        p5 += 1
    elif 600 <= a <= 799:
        p4 += 1
    elif 400 <= a <= 599:
        p3 += 1
    elif 200 <= a <= 399:
        p2 += 1
    else:
        p1 += 1

p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
p4 = p4 / n * 100
p5 = p5 / n * 100

print('{:.2f}'.format(p1) + "%")
print('{:.2f}'.format(p2) + "%")
print('{:.2f}'.format(p3) + "%")
print('{:.2f}'.format(p4) + "%")
print('{:.2f}'.format(p5) + "%")