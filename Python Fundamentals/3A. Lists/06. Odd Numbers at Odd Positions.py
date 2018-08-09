data = list(map(int, input().split(" ")))

odd_data = []

for item in range(0, len(data)):
    if item % 2 != 0 and data[item] % 2 != 0:
        odd_data.append(item)
        print(f"Index {item} -> {data[item]}")
