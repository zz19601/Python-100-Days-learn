"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""
import math

def perimeter(radius):
    p = math.pi * radius * 2
    return p
def area(radius):
    a = math.pi * radius * radius
    return a

def main():
    radius = float(input('please input the length of radius you want: '))
    print('the perimeter is: ' + str(perimeter(radius)))
    print('the area is: ' + str(area(radius)))
    quit()

main()