import os
import pathlib
import random
import string

def create_and_rename_images():
    current_directory = pathlib.Path(__file__).parent

    img_directory = current_directory / "img"
    img_directory.mkdir(exist_ok=True)

    file_names = set()
    while len(file_names) < 100:
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + ".png"
        file_names.add(file_name)

    for file_name in file_names:
        file_path = img_directory / file_name
        with open(file_path, 'w') as file:
            file.write("This is a sample image file.")

    print("img目录及其中的100个文件创建完成。")

    all_files = list(img_directory.glob("*"))
    random.shuffle(all_files)
    for i, file_path in enumerate(all_files):
        if i < 50:
            new_file_path = file_path.with_suffix(".jpg")
            file_path.rename(new_file_path)

    print("50个文件的扩展名已改为.jpg。")

create_and_rename_images()

