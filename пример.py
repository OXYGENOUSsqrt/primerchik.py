from math import *

a = float (input('Введите a: '))
x = float (input('Введите x: '))
b = float (input('Введите b: '))

y = (pow((a + 1 / log ( abs ( sin (x) + cos ( log ( abs (a * x - b)))))),2) / pow(tan(pow(log(2 * x), 2)), 2))
print (f'Значение y = {y} ')