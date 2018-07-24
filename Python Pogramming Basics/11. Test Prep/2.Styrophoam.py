import math
budget = float(input())
area = float(input())
windows = int(input())
sq_m_per_packet = float(input())
price = float(input())

area = area - windows * 2.4
area = area * 1.1
packet = math.ceil(area / sq_m_per_packet)

total_price = packet * price
left = abs(total_price - budget)
if budget >= total_price:
    print(f"Spent: {total_price:.2f}")
    print(f"Left: {left:.2f}")
else:
    print(f"Need more: {left:.2f}")


