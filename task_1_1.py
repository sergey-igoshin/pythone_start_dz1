name = input('Введите имя: ')
year = int(input('Ваш год рождения: '))
age = 2021 - year
message = age % 10
if message == 1:
    message = 'год'
elif 1 > message > 5:
    message = 'года'
else:
    message = 'лет'
print(f'\n{name} ваш возраст {age} {message}')
