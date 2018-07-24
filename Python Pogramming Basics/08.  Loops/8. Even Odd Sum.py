import math
n = int(input())
odd_sum = 0
even_sum = 0

for i in range(0, n):
    a = int(input())
    if i % 2 == 1:
        odd_sum = odd_sum + a
    else:
        even_sum = even_sum + a

if odd_sum == even_sum:
    print("Yes, sum = %d" % odd_sum)
else:
    print("No, diff = %d" % math.fabs(even_sum - odd_sum))
