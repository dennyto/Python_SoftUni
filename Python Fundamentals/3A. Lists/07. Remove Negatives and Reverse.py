data = list(map(int, input().split(" ")))

for item in data:
    if item < 0:
        data.remove(item)

print(reversed(data))
