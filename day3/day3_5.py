nian = int(input("请输入任意年份"))

if nian % 100 == 0:
    if nian % 400 == 0:
        print(f"{nian}年是闰年")
    else:
        print(f"{nian}不是闰年")
else:
    if nian % 4 == 0:
        print(f"{nian}是闰年")
    else:
        print(f"{nian}不是闰年")
