import random
import string

def generate_random_line():
    line_length = random.randint(1, 50)
    line = ''.join(random.choice(string.printable) for _ in range(line_length))
    return line

def create_and_copy_file(file_name, copy_file_name, num_lines):
    with open(file_name, 'w') as file:
        for _ in range(num_lines):
            line = generate_random_line()
            file.write(line + '\n')

    with open(file_name, 'r') as source_file, open(copy_file_name, 'w') as target_file:
        target_file.write(source_file.read())

num_lines = int(input("请输入要生成的行数: "))

create_and_copy_file('test.txt', 'copy_test.txt', num_lines)

print(f"{num_lines} 行内容已生成并复制到 copy_test.txt 文件中。")
