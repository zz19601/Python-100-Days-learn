sum = 0
for i in range (10000):
    for j in range (1,i):
        if (i%j == 0):
            sum += j
    if (sum == i):
        print (str(sum)+' ')
    sum = 0