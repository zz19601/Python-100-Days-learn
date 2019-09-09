#### 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

import random

def token(n):
    allSet = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

    tokenCharSet = ''
    for i in range (int(n)):
        pick = random.randint(0,len(allSet)-1)
        tokenCharSet += allSet[pick]
    return tokenCharSet
    
print(token(input('the number you want: ')))