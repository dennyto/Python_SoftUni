data_string = input().split(" ")
data_dict = {}

for item in data_string:
    if item.lower() in data_dict:
        data_dict[item.lower()] += 1
    else:
        data_dict[item.lower()] = 1

output = ""
for item in data_dict:
    if data_dict[item] % 2 != 0:
        output += item + ", "

print(output.strip(", "))








