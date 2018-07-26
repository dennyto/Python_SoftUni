number = abs(int(input()))


def add_even_numbers(a):
    even = 0
    while a != 0:
        last_digit = a % 10
        if last_digit % 2 == 0:
            even += last_digit
        a = a // 10
    return even


def add_odd_numbers(b):
    odd = 0
    while b != 0:
        last_digit = b % 10
        if last_digit % 2 != 0:
            odd += last_digit
        b = b // 10
    return odd


def multiplication(input_num):
    end_result = add_even_numbers(input_num) * add_odd_numbers(input_num)
    return end_result


print(multiplication(number))



