list_num = list(range(101, 200))
list_su = []
list_he = []

for num in range(101, 201):
    for value in range(2, num):
        if num % value == 0:
            list_he.append(num)
            break

for num in list_num:
    if num not in list_he:
        list_su.append(num)

print(list_su)
