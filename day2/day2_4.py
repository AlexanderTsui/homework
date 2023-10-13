sxhs = []
sum = 0

for num in range(100, 1000):
    hundreds_digit = num // 100
    tens_digit = (num % 100) // 10
    ones_digit = num % 10
    sum = hundreds_digit ** 3 + tens_digit ** 3 + ones_digit ** 3
    if sum == num:
        sxhs.append(num)

print(sxhs)