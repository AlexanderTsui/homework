a = int(input("请输入a的值"))
A = int(a)
num = int(input("请输入您希望几个数求和"))
count = 0
s = 0
aim_weishu = 0
now_weishu = 1

while count < num:
    count += 1
    aim_weishu += 1
    while now_weishu < aim_weishu:
        now_weishu += 1
        a = a * 10 + A
        print(a)
    s += a

print(f"s的值为：{s}")
