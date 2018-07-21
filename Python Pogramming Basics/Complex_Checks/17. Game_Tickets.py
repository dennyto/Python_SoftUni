budget = float(input())
category = input()
people = int(input())

if people <= 4:
    travel = budget * 0.75
elif 4 < people <= 9:
    travel = budget * 0.6
elif 9 < people <= 24:
    travel = budget * 0.5
elif 24 < people <= 49:
    travel = budget * 0.4
else:
    travel = budget * 0.25

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

less_travel = budget - travel
total_tickets = ticket_price * people
left_over = less_travel - total_tickets

if left_over < 0:
    left_over = abs(left_over)
    print("Not enough money! You need " + '{:.2f}'.format(left_over) + " leva.")
else:
    print("Yes! You have " + '{:.2f}'.format(left_over) + " leva left.")



