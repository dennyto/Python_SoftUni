h = float(input())
x = float(input())
y = float(input())

if h < x < h*2 and y == h:
    print("Inside")
elif (0 <= x <= h*3 and (y == h or y == 0)) or (0 <= y <= h and (x == 0 or x == h*3)):
    print("Border")
elif (h <= x <= h*2 and (y == h or y == h*4)) or (h <= y <= h*4 and (x == h or x == h*2)):
    print("Border")
elif (0 < x <h*3 and 0 < y < h) or ( h < x < h*2 and 0 < y < h*4):
    print("Inside")
else:
    print("Outside")








