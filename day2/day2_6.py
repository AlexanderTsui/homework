list = []
n = int(input("请输入一个正整数"))
divisor = 2
text = str(n)
text = f"{text} = "

while divisor <= n:
    if n % divisor == 0:
        list.append(divisor)
        n = n // divisor
    else:
        divisor += 1

for factor in list:
    text = f"{text}{factor} * "

text = text[:-2]
print(text)
