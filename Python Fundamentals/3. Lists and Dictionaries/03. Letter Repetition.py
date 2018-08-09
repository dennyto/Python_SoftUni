data_string = input()
data_dict = {}

for item in data_string:
    if item in data_dict:
        data_dict[item] += 1
    else:
        data_dict[item] = 1

print(data_dict)

for item in data_dict.keys():
    print(f"{item} -> {data_dict[item]}")

