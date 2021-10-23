income = int(input('Введите доход компании: '))
expense = int(input('Введите расход компании: '))
spread = income - expense
profitability = spread / income
if spread <= 0:
    print(f'Финансовый результат компании -\033[1;31m "Отрицательный"')
else:
    print(f'Финансовый результат компании -\033[1;32m "Положительный"\n\033[0;0m'
          f'Рентабельность компании - {profitability * 100: 0.1f}%')
    stat = int(input('Введите кол-во сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника - {spread / stat: 0.2f}')
