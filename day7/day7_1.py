import random
import numpy as np

def process_data(filename):
    data = [[random.random() for _ in range(3)] for _ in range(10)]

    with open(filename, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

    data = np.genfromtxt(filename, delimiter=',')

    second_column = data[:, 1]

    max_value = np.max(second_column)
    min_value = np.min(second_column)
    average_value = np.mean(second_column)
    median_value = np.median(second_column)

    return max_value, min_value, average_value, median_value

max_val, min_val, avg_val, median_val = process_data('data.txt')

print(f"第二列的最大值: {max_val}")
print(f"第二列的最小值: {min_val}")
print(f"第二列的平均值: {avg_val}")
print(f"第二列的中位数: {median_val}")
