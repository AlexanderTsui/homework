n = int(input("请输入任意正整数"))
str_n = str(n)
my_list = []
text = ""
for char in str_n:
    my_list.insert(0, char)

cishu = len(my_list) // 2
yxcs = 0
panding = True

while yxcs < cishu:
    yxcs += 1
    if my_list[0] != my_list[-1]:
        print(f"{str_n}不是回文数")
        panding = False
        break
    else:
        del my_list[0]
        del my_list[-1]

if panding:
    print(f'{str_n}是回文数')
