import math

for i in range(100, 1000):
    digit1 = int(str(i)[0])
    digit2 = int(str(i)[1])
    digit3 = int(str(i)[2])
    if (math.pow(digit1, 3) + math.pow(digit2, 3) + math.pow(digit3, 3)) == i:
        print (i)
        print('  ')
    else:
        continue
    





