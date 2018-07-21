days = int(input())

daysOff = days * 127
workDays = (365 - days) * 63
totalPlay = daysOff + workDays
difference = abs(totalPlay - 30000)
hrs = difference // 60
mins = difference % 60

if totalPlay < 30000:
    print("Tom sleeps well")
    print(str(hrs) + " hours and " + str(mins) + " minutes less for play")
else:
    print("Tom will run away")
    print(str(hrs) + " hours and " + str(mins) + " minutes more for play")
# print("{} hours and {} minutes {} for play".format(hrs, mis, play_str))
