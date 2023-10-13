#这段代码的目的是删除列表中的所有奇数元素，但存在一个问题，即在遍历列表时修改了列表的长度，这会导致索引 idx 不准确，循环中漏掉了一些元素。
#这是因为每次删除奇数元素后，列表的长度会减少，但循环的索引 idx 会继续递增，导致一些元素被跳过。

#这是修改后的代码：
my_list = list(range(1000))

even_list = []

for num in my_list:
    if num % 2 == 0:
        even_list.append(num)

my_list = even_list

print(my_list)


