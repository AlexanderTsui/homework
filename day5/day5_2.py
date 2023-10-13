def function(list):
    count = 0
    final_list = []
    for i in list:
        count += 1
        if count % 2 == 1:
            final_list.append(i)
    print(final_list)

#以下为测试代码：`
list = [12,578,53,9,4,8,3,15,4]
print(list)
function(list)
