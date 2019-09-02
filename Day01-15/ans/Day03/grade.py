"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
Author: 骆昊
"""

def transfer(grades):
    if 90 <= grades:
        return 'A'
    elif 80 <= grades <=89:
        return 'B'
    elif 70 <= grades <=79:
        return 'C'
    elif 60 <= grades <=69:
        return 'D'
    elif grades < 60:
        return 'E'

grades = int(input('请输入分数'))
print('您的G点是： ' + str(transfer(grades)))