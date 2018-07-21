bitCoins = float(input())
chin = float(input())
comm = float(input())

bitLev = bitCoins * 1168
chinLev = chin * 0.15 * 1.76
euro = (bitLev + chinLev)/1.95
euroFinal = euro - euro * comm/100
print("{0:.2f}".format(euroFinal))
