num_user = int(input('Введите положительное число: '))
num = num_user
max_num = 0
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
    num = num // 10
print(f'В числе "{num_user}" -> максимальное число "{max_num}"')
