import os


def process_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()

    if 'python' in file_path:
        new_file_path = file_path.replace('python', 'class')
        os.rename(file_path, new_file_path)

    if 'python' in file_contents:
        new_file_contents = file_contents.replace('python', 'class')
        with open(file_path, 'w') as file:
            file.write(new_file_contents)


for root, dirs, files in os.walk("test"):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        process_file(file_path)

print("替换完成。")
