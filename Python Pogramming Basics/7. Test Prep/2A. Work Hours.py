hours_needed = float(input())
workers = int(input())
workdays = int(input())

total_hours = workers * workdays * 8
left = abs(total_hours - hours_needed)

if total_hours >= hours_needed:
    print(f"{left:.0f} hours left")
else:
    penalty = workdays * left
    print(f"{left:.0f} overtime")
    print(f"Penalties: {penalty:.0f}")

