"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: zz
"""
import os

def compYear(year):
    if(year%4  == 0):
        return ('闰年')
    else:
        return('非闰年')

def checkResult():
    year = int(input('input the year you want to check: '))
    print(compYear(year))

def checkIfEnd():
    ifEnd = input('是否结束(请输入1 or 0)： ')
    if (ifEnd == '1'):
        checkResult()
        checkIfEnd()
    else:
        print('thank you, bye')
        os._exit(1)
checkResult()
checkIfEnd()