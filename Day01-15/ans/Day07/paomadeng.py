#### 练习1：在屏幕上显示跑马灯文字
import os
import time

def horse(n):
    temp = ''
    i = 0
    while i <= len(n):
        os.system('cls')
        temp += n[i]
        print (temp)
        time.sleep(1)
        i += 1
        if i == (len(n)):
            i = 0
            temp = ''

n = input('please input your words: ')
horse(n)