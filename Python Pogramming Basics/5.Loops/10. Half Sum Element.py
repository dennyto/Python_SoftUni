import math
max_num = float('-inf')
n = int(input())
total = 0

for i in range(0, n):
    a = int(input())
    total += a
    if a > max_num:
        max_num = a

if max_num == total / 2:
    print("Yes, sum = %d" % max_num)
else:
    print("No, diff = %d" % math.fabs(total - max_num * 2))
