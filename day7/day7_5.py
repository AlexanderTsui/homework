import os
import random
import string

i = int(input("请输入要创建的文件个数（i）："))
j = int(input("请输入每个文件要写入的随机行数（j）："))

os.makedirs("test", exist_ok=True)

def generate_random_string():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

for file_num in range(1, i + 1):
    filename = f"test/file_{file_num}.txt"
    with open(filename, "w") as file:
        for _ in range(j):
            file.write(generate_random_string() + "\n")

for root, dirs, files in os.walk("test"):
    for file_name in files:
        file_path = os.path.join(root, file_name)

        new_file_name = file_name + "-python"
        os.rename(file_path, os.path.join(root, new_file_name))

        with open(os.path.join(root, new_file_name), "a") as file:
            file.write("-python")

print("操作完成。")
