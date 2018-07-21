import math
n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    a = int(input())
    left_sum = left_sum + a

for i in range(0, n):
    a = int(input())
    right_sum = right_sum + a

if left_sum == right_sum:
    print("Yes, sum = %d" % left_sum)
else:
    print("No, diff = %d" % math.fabs(right_sum - left_sum))
