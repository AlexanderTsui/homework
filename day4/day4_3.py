input_str1 = input("请输入3*3矩阵的第一行")
numbers1 = input_str1.split(",")

if len(numbers1) == 3:
    num1 = int(numbers1[0])
    num2 = int(numbers1[1])
    num3 = int(numbers1[2])
else:
    print("输入的格式不正确，请输入三个用逗号隔开的数字。")

input_str2 = input("请输入3*3矩阵的第二行")
numbers2 = input_str2.split(",")

if len(numbers2) == 3:
    num4 = int(numbers2[0])
    num5 = int(numbers2[1])
    num6 = int(numbers2[2])
else:
    print("输入的格式不正确，请输入三个用逗号隔开的数字。")

input_str3 = input("请输入3*3矩阵的第三行")
numbers3 = input_str3.split(",")

if len(numbers3) == 3:
    num7 = int(numbers3[0])
    num8 = int(numbers3[1])
    num9 = int(numbers3[2])
else:
    print("输入的格式不正确，请输入三个用逗号隔开的数字。")

print(f"X = \n[{num1} {num2} {num3}]\n[{num4} {num5} {num6}]\n[{num7} {num8} {num9}]")

input_str4 = input("请输入3*3矩阵的第一行")
numbers4 = input_str4.split(",")

if len(numbers4) == 3:
    num10 = int(numbers4[0])
    num11 = int(numbers4[1])
    num12 = int(numbers4[2])
else:
    print("输入的格式不正确，请输入三个用逗号隔开的数字。")

input_str5 = input("请输入3*3矩阵的第二行")
numbers5 = input_str5.split(",")

if len(numbers5) == 3:
    num13 = int(numbers5[0])
    num14 = int(numbers5[1])
    num15 = int(numbers5[2])
else:
    print("输入的格式不正确，请输入三个用逗号隔开的数字。")

input_str6 = input("请输入3*3矩阵的第三行")
numbers6 = input_str6.split(",")

if len(numbers6) == 3:
    num16 = int(numbers6[0])
    num17 = int(numbers6[1])
    num18 = int(numbers6[2])
else:
    print("输入的格式不正确，请输入三个用逗号隔开的数字。")

print(f"X + Y = \n[{num1 + num10} {num2 + num11} {num3 + num12}]\n[{num4 + num13} {num5 + num14} {num6 + num15}]\n[{num7 + num16} {num8 + num17} {num9 + num18}]")