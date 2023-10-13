with open('test.txt', 'r') as file1, open('copy_test.txt', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

different_lines = []
for i, (line1, line2) in enumerate(zip(lines1, lines2)):
    if line1 != line2:
        different_lines.append(i + 1)

print("不同的行编号：", different_lines)
