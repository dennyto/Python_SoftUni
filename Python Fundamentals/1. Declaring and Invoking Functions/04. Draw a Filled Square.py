size = int(input())


def top_bottom_rows(a):
    print("-" * a * 2)


def middle_rows(b):
    for i in range (0, b-2):
        print("-" + "\\/" * (b-1) + "-")


top_bottom_rows(size)
middle_rows(size)
top_bottom_rows(size)

