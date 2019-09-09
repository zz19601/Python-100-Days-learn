#### 练习3：设计一个函数返回给定文件名的后缀名。

def postfix(fileName):
    index = len(fileName) - 1
    postfixName = ''
    while True:
        if fileName[index] != '.':
            postfixName += fileName[index]
            index -= 1
        else:
            return postfixName[::-1]

print(postfix(input('input the file name: ')))
            
