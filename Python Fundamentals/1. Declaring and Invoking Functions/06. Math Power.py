a = float(input())
b = int(input())


def math_pow(c, d):
    result = 1
    for i in range(1, d + 1):
        result = result * c
    return result


print(math_pow(a, b))
