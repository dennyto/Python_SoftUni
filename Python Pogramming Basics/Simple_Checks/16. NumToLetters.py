n = int(input())
teen = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen", "twenty"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety", "one hundred"]
small = n % 10
big = n // 10

if n < 0 or n > 100:
    print("invalid number")
elif 0 <= n <= 20:
    print(teen[n])
elif small == 0:
    print(tens[big-2])
else:
    print(tens[big-2], teen[small])


