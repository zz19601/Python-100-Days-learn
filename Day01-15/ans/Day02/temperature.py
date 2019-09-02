"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: zz
"""


def transfer(c = 1.0):
    f = 1.8 * c + 32
    return f
c = float(input('please input c: '))
print('F = '+str(transfer(c))+' when C = '+ str(c))
quit()