n1 = int(input())
n2 = int(input())
action = input()
result = 0

if action == "+":
    result = n1 + n2
elif action == "-":
    result = n1 - n2
elif action == "*":
    result = n1 * n2
elif action == "/":
    if n2 != 0:
        result = n1 / n2
    else:
        pass
elif action == "%":
    if n2 != 0:
        result = n1 % n2
    else:
        pass

if n2 == 0:
    print("Cannot divide " + str(n1) + " by zero")
elif (action == "+" or action == "-" or action == "*") and result % 2 == 0:
    print(str(n1) + " " + action + " " + str(n2) + " = " + str(result) + " - " + "even")
elif (action == "+" or action == "-" or action == "*") and result % 2 != 0:
    print(str(n1) + " " + action + " " + str(n2) + " = " + str(result) + " - " + "odd")
elif action == "/":
    print(str(n1) + " " + action + " " + str(n2) + " = " + '{:.2f}'.format(result))
elif action == "%":
    print(str(n1) + " " + action + " " + str(n2) + " = " + str(result))




