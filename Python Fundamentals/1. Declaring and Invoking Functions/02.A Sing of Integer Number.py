def print_sign(num):
    if num > 0:
        print("The number {0} is positive.".format(num))​
    elif num < 0:
        print("The number {0} is negative.".format(num))​
    else:
        print("The number {0} is zero.".format(num))​


print_sign(int(input()))