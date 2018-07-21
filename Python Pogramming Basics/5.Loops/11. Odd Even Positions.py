n = int(input())
OddMin = int(1000000000)
EvenMin = int(1000000000)
OddMax = int(-1000000000)
EvenMax = int(-1000000000)
OddSum = 0
EvenSum = 0

for i in range(1, n+1):
    a = float(input())
    if i % 2 == 1:
        OddSum += a
        if a > OddMax:
            OddMax = a

        if a < OddMin:
            OddMin = a
    else:
        EvenSum += a
        if a > EvenMax:
            EvenMax = a

        if a < EvenMin:
            EvenMin = a

print("OddSum=%g" % OddSum)

if OddMin == int(1000000000):
    print("OddMin=No")
else:
    print("OddMin=%g" % OddMin)

if OddMax == int(-1000000000):
    print("OddMax=No")
else:
    print("OddMax=%g" % OddMax)

print("EvenSum=%g" % EvenSum)

if EvenMin == int(1000000000):
    print("EvenMin=No")
else:
    print("EvenMin=%g" % EvenMin)

if EvenMax == int(-1000000000):
    print("EvenMax=No")
else:
    print("EvenMax=%g" % EvenMax)





