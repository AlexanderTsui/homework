shulie = [0,1]
count = 0
tmp_1 = 0
tmp_2 = 0
newnum =0

while count <= 17:
    count += 1
    tmp_1 = shulie[-1]
    tmp_2 = shulie[-2]
    newnum = tmp_1 + tmp_2
    shulie.append(newnum)

print(shulie)