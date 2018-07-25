b = float(input())
h = float(input())


def calculate_triangle(a, c):
    result = a * c / 2
    return result


area = calculate_triangle(b, h)
print(f"{area:.12g}")

