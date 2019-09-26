#### 计算指定的年月日是这一年的第几天

def dateAddr(year, month, date):
    monthCount = {'Jan':0, 'Feb':31, 'Mar':59, 'Apr':90, 'May':120, 'June':151, 'July':181, 'Aug':212, 'Sep':243, 'Oct':273,'Nov':304, 'Dec':334}
    dateAddress = monthCount[month] + int(date)
    if (int(year)%4 == 0) & (month not in ['Jan', 'Feb']):
        dateAddress += 1
    return dateAddress

year = input('year: ')
month = input('monter: ')
date = input('date: ')
print(str(dateAddr(year,month,date)))