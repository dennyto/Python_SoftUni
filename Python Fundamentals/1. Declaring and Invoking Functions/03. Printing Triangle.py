num = int(input())


def print_triangle(a):
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            print(str(j) + " ", end='')
        print()
    for i in range(num - 1, 0, -1):
        for j in range(1, i + 1):
            print(str(j) + " ", end='')
        print()


print_triangle(num)
