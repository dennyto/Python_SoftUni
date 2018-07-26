type_of = input()
a = input()
b = input()


def int_type(c, d):
    if int(c) > int(d):
        return c
    else:
        return d


def char_type(c, d):
    if ord(c) > ord(d):
        return c
    else:
        return d


def string_type(c, d):
    if c > d:
        return c
    else:
        return d


if type_of == "int":
    print(int_type(a, b))
elif type_of == "char":
    print(char_type(a, b))
else:
    print(string_type(a, b))




