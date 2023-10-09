correct_nums = []
for num_3 in range(1,5):
    for num_2 in range(1,5):
        for num_1 in range(1,5):
            if num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
                num_temporary = num_1 + num_2 * 10 + num_3 * 100
                correct_nums.append(num_temporary)
print(f"共有{len(correct_nums)}个三位数")
print("分别为：")
print(correct_nums)