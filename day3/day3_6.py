nian = int(input("请输入任意年份："))
yue = int(input("请输入月份："))
ri = int(input("请输入日期："))
tianshu = 0
runnian = False

if nian % 100 == 0:
    if nian % 400 == 0:
        runnian = True
else:
    if nian % 4 == 0:
        runnian = True

for value in range(1, yue):
    if value == 1 or value == 3 or value == 5 or value == 7 or value == 8 or value == 10 or value == 12:
        tianshu += 31
    elif value == 4 or value == 6 or value == 9 or value == 11:
        tianshu += 30
    else:
        if runnian:
            tianshu += 29
        else:
            tianshu += 28

tianshu += ri

print(f"这一天是一年的第{tianshu}天")
