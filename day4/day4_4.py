import random

n = int(input("请输入 n 的值: "))
m = int(input("请输入 m 的值: "))

random_list = [random.randint(1, 100) for _ in range(n)]

print("原始列表:", random_list)

for _ in range(m):
    element = random_list.pop(-1)
    random_list.insert(0, element)

print("处理后的列表:", random_list)
