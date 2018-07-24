age = int(input())
washing_mashine = float(input())
toy_price = int(input())
bonus = 10
brother_money = 0
toys = 0
total = 0

for i in range(1, age + 1):
    if i % 2 == 1:
        toys += 1
    else:
        total += bonus
        bonus += 10
        brother_money += 1

total = total + toys * toy_price - brother_money

diff = total - washing_mashine

if diff >= 0:
    print("Yes! {:.2f}".format(diff))
else:
    print("No! {:.2f}".format(-diff))
