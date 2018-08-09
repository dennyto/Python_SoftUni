data_string = input()

data_dict = {}

while not data_string == "end":
    data_string = data_string.split(" = ")
    if data_string[1].isnumeric():
        data_dict[data_string[0].strip(" ")] = int(data_string[1].strip(" "))

    if data_string[1].strip(" ") in data_dict.keys():
        new_value = data_dict.get(data_string[1].strip(" "))
        if new_value:
            data_dict[data_string[0].strip(" ")] = new_value

    data_string = input()

for item in data_dict:
    print(f"{item} === {data_dict[item]}")



