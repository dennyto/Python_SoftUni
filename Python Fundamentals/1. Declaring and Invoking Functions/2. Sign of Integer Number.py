number = int(input())
result = None


def sign_function(num):
    if num > 0:
        result = "positive"
    elif num < 0:
        result = "negative"
    else:
        result = "zero"
    return result


print(f"The number {number} is {sign_function(number)}")
