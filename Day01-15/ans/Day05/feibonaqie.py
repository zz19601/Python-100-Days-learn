##F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

def fibonacci(n):
    f1 = 1
    f2 = 1
    print (str(f1))
    print (str(f2))
    for i in range (n):
        print (f1 + f2)
        temp = f1
        f1 = f2
        f2 = f1 + temp
fibonacci(10)