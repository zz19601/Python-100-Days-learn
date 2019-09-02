## 5m+3f+1/3c = 100
## m+f+c = 100
## 5m + 3f +1/3(100-m-f) = 100
## 14m + 8f  = 200
## 7m + 4f = 100

for m in range (100):
    for f in range (100 - m):
        if (7 * m + 4 * f == 100):
            print (str(m) + ' ' + str (f) + ' ' + str(100-f-m))
