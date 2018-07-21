amount = float(input())
original = input()
original_to_bg = 1.0
to_currency = input()

if original != "BGN":
    if original == "EUR":
        original_to_bg = amount * 1.95583

    elif original == "USD":
        original_to_bg = amount * 1.79549

    elif original == "GBP":
        original_to_bg = amount * 2.53405

else:
    original_to_bg = amount

# Beginning of second step# if to_currency == "EUR":

if to_currency == "EUR":
    result = original_to_bg / 1.95583

elif to_currency == "USD":
    result = original_to_bg / 1.79549

elif to_currency == "GBP":
    result = original_to_bg / 2.53405

else:
    result = original_to_bg


print(round(result,2), to_currency)

