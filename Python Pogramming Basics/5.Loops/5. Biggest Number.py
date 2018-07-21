max_num = float('-inf')
n = int(input())

for i in range(1, n +1):
    a = float(input())
    if a > max_num:
        max_num = a

print(int(max_num))
