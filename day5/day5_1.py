def calculate(*num):
    sum = 0
    for i in num:
        sum += i
    average = sum / len(num)
    count = -1
    tmp_list = [average]
    for i in num:
        count += 1
        if i > average:
            tmp_list.append(count)

    yuanzu = tuple((average,tmp_list))
    print(yuanzu)

#以下为测试代码：

user_input = input("请输入用逗号隔开的四个数字: ")

input_list = user_input.split(',')

if len(input_list) != 4:
    print("请输入三个数字，用逗号隔开")
else:
    num1, num2, num3, num4 = map(float, input_list)

calculate(num1, num2, num3, num4)
