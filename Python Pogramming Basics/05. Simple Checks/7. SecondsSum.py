player1 = int(input())
player2 = int(input())
player3 = int(input())
total = player1 + player2 + player3

minutes = total // 60
secs = total % 60

if secs < 10:
    print(str(minutes) + ':0' + str(secs))
else:
    print(str(minutes)+":"+str(secs))
