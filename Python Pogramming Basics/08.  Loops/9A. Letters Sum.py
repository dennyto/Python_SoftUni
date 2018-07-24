word = input().lower()
total = 0

for i in range(0, (len(word) - 1)):
    if word[i] == "a":
        total += 1
    elif word[i] == "e":
        total += 2
    elif word[i] == "i":
        total += 3
    elif word[i] == "o":
        total += 4
    elif word[i] == "u":
        total += 5

print(total)
