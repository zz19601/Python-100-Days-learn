#### 练习2：实现判断一个数是不是回文数的函数。

def palindrome(n):
    temp = n
    reverse = 0
    while temp > 0:
        reverse = reverse*10 + temp%10
        temp = temp//10
        print (reverse)
        print (temp)
    return (reverse == n)

n = int(input('n='))
print (str(palindrome(n)))