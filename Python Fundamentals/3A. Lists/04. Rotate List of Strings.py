data = input().split(" ")
last_item = data.pop()
new_data = []

new_data.append(last_item)
new_data.extend(data)

for item in new_data:
    print(item, end=" ")


