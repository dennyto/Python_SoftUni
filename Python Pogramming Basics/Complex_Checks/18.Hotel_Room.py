month = input()
nights = int(input())
total_studio = 0
total_apt = 0
discount_studio = 1
discount_apt = 1

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apt = 65
elif month == "June" or month == "September":
    price_per_night_studio = 75.2
    price_per_night_apt = 68.7
elif month == "July" or month == "August":
    price_per_night_studio = 76
    price_per_night_apt = 77

if nights > 14:
    discount_apt = 1 - 0.1
    if month == "June" or month == "September":
        discount_studio = 1 - 0.2
    elif month == "May" or month == "October":
        discount_studio = 1- 0.3
elif 7 < nights <= 14:
    if month == "May" or month == "October":
        discount_studio = 1 - 0.05

total_apt = nights * price_per_night_apt * discount_apt
total_studio = nights * price_per_night_studio * discount_studio

print("Apartment: " + '{:.2f}'.format(total_apt) + " lv.")
print("Studio: " + '{:.2f}'.format(total_studio) + " lv.")
