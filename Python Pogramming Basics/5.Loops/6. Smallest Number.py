min_num = float('inf')
n = int(input())

for i in range(1, n +1):
    a = float(input())
    if a < min_num:
        min_num = a

print(int(min_num))
