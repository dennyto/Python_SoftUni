N = int(input())
W = float(input())
L = float(input())
M = float(input())
O = float(input())

number = (N * N - M * O) / (W * L)
time = number * 0.2
print("{0:.2f}".format(number))
print("{0:.2f}".format(time))
