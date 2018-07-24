n = int(input())
a = 1
b = 2

for i in range(1, (n + 1)//2 + 1):
    if n % 2 == 1:
        d = n//2 - i + 1
        print("-" * d + "*" * a + "-" * d)
        a += 2
    else:
        print("-" * (n - i - 3) + "*" * b + "-" * (n - i - 3))
        b += 2
c = n // 2

for i in range(0, c):
    print("|" + "*" * (n - 2) + "|")
