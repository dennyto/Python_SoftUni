data_string = input().split(" ")
data_dict = {}

for item in data_string:
    if item.lower() in data_dict:
        data_dict[item.lower()] += 1
    else:
        data_dict[item.lower()] = 1

print(data_dict)

for item in sorted(data_dict.keys()):
    print(f"{item} -> {data_dict[item]} times")


