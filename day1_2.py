x = int(input("请输入x的值"))
y = int(input("请输入y的值"))
z = int(input("请输入z的值"))
tmp = 0
while True:
    if x > y:
        tmp = x
        x = y
        y = tmp
    elif y > z:
        tmp = y
        y = z
        z = tmp
    else:
        break

print(f"排序后的结果为：{x}，{y}，{z}。")
