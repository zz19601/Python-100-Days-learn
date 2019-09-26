#### 设计一个函数返回传入的列表中最大和第二大的元素的值。

def max(numList):
    numList.sort()
    return numList[-1]
def sec(numList):
    numList.sort()
    return numList[-2]

numList = ['a','b','oa','p']
print(str(max(numList))+'  '+str(sec(numList)))