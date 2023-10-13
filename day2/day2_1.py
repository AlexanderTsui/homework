line = input("请输入一行字符")
line = line.replace("\n", "")

letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

for char in line:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

print("字母个数:", letter_count)
print("数字个数:", digit_count)
print("空格个数:", space_count)
print("其他字符个数:", other_count)
