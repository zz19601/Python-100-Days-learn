#### 练习1：实现计算求最大公约数和最小公倍数的函数。

def greatestCommonDivisor(n=1,m=1):
    if (n%m==0):
        return m
    else:
        return greatestCommonDivisor(m, n%m)

def leastCommonMultiple(n=1,m=1):
    gcd = greatestCommonDivisor(n,m)
    return (n*m/gcd)

n = int(input ('n='))
m = int(input ('m='))

print (str(greatestCommonDivisor(n,m)))
print (str(leastCommonMultiple(n,m)))