count_hang = 0
count_lie = 0
while count_hang <= 8:
    count_hang += 1
    while count_lie <= count_hang:
        count_lie += 1
        if count_lie < count_hang:
            print(f"{count_lie}*{count_hang}={count_hang * count_lie}",end=' ')
        elif count_lie == count_hang:
            print(f"{count_lie}*{count_hang}={count_hang * count_lie}")
    count_lie = 0