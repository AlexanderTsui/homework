n = int(input("请输入任意正整数"))
str_n = str(n)
my_list = []
text = ""
for char in str_n:
    my_list.insert(0, char)

print(f"该数为{len(my_list)}位数")

for value in my_list:
    text = f"{text}{value}"

print(f"该数的逆序为：{text}")
