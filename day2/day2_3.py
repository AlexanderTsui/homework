height = 100
aim_cishu = 10
now_cishu = 0
path = 0
while now_cishu < aim_cishu:
    now_cishu += 1
    path += height
    height = height * 0.5
    path += height
    print(f"第{now_cishu}次弹跳，路程为：{path}，高度为：{height} (修正前)")

path = path - height
print(f"第{now_cishu}次弹跳，路程为：{path}，高度为：{height} (修正后)")
