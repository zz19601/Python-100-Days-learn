"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: zz
"""
def transfer():
    danwei = input('请输入单位: ')
    quantity = float(input('请输入数量： '))
    if danwei == 'inch':
        result = quantity*2.54
    elif danwei == 'cm':
        result = quantity/2.54
    else:
        return ('请输入正确单位')
        transfer()
    return result

outp = str(transfer())
print('the result is: ' + outp)

