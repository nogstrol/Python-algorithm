print('Введите координаты точки А(х1, у1):')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))


print('Введите координаты точки B(x2, y2):')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('Уравнение прямой проходящей через эти точки')
if x1 == x2:
    print(f'x = {x1:.3f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.3f} * x + {b:.3f}')