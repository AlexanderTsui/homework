import random

def create_random_integer_file():
    with open('data.txt', 'w') as file:
        for _ in range(100000):
            random_integer = str(random.randint(1, 100))
            file.write(random_integer + '\n')

    print("文件 data.txt 创建完成。")

create_random_integer_file()

