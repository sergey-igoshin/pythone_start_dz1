duration = int(input('Введите кол-во секунд: '))
minute = 60
hour = minute * 60
day = hour * 24

s = duration % 60
m = duration // minute % 60
h = duration // hour % 24
d = duration // day
print(f'{"%02d" % d}:{"%02d" % h}:{"%02d" % m}:{"%02d" % s}')
