import random

sorted_list = [random.randint(1, 100) for _ in range(10)]
sorted_list.sort()

print("已排序的数组:", sorted_list)

new_number = int(input("请输入一个数: "))

index = 0
while index < len(sorted_list) and sorted_list[index] < new_number:
    index += 1

sorted_list.insert(index, new_number)

print("插入后的数组:", sorted_list)
