import os

os.makedirs("img", exist_ok=True)

for i in range(1, 101):
    filename = f"X{i}.png"
    file_path = os.path.join("img", filename)

    with open(file_path, "w"):
        pass

print("创建完成。")
