__author__ = 'Denisova E.'
#Даны два действительных положительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.
a = float(input ('Введите число a (действительное положительное): '))
b = float(input ('Введите число b (действительное положительное): '))

m = (a + b) / 2.0
s = (a * b) ** 0.5

print ('Среднее арифметическое a и b = ', m)
print ('Среднее геометрическое a и b = ', s)