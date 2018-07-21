hour = int(input())
mins = int(input())

total = hour * 60 + mins + 15

finalHour = total // 60
finalMins = total % 60

if finalHour >= 24:
    finalHour = finalHour - 24

if finalMins >= 10:
    print(str(finalHour) + ":" + str(finalMins))
else:
    print(str(finalHour) + ":0" + str(finalMins))
