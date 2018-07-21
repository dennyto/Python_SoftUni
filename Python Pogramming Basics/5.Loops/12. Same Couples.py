n = int(input())
first_sum = 0
second_sum = 0
last_sum = 0
biggest_diff = float(0)

for i in range(1, n+1):
    a = float(input())
    b = float(input())
    second_sum = a + b
    if i == 1:
        first_sum = second_sum

    if biggest_diff < abs(first_sum - second_sum):
        biggest_diff = abs(first_sum - second_sum)

    first_sum = second_sum

if biggest_diff == 0:
    print("Yes, value={:.0f}".format(second_sum))
else:
    print("No, maxdiff={:.0f}".format(biggest_diff))

