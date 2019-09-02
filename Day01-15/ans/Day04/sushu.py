"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: zz
Date:--
"""

def sushu(integer):
    for i in range(2, int(integer) - 1):
        if int(integer)%i == 0:
            return ('not sushu')
        return ('sushu')

def main():
    x = input('please input the integer you want: ')
    print ('it is ' + str(sushu(x)))

main()