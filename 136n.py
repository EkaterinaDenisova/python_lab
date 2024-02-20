__author__ = 'Denisova E.'
#Даны натуральное число n, действительные числа a1,..., an. Вычислить:

import unit

unit.test_calc_result()

n = int(input("Введите число элементов массива (целое число): "))

#генератор списка
# a = [  float(input("Введите элемент массива: ")) #выражение для вычисления элементов списка (ввод пользователем)
#        for i in range(n) #цикл повторяет выражение
#        ]

a = unit.rnd_list_float(n, -100, 100)

# r = 0.0

# for i in range (n):
# 	r += (math.sqrt(abs(a[i])) - a[i])**2

r = unit.calc_result136(a)

print (f"Результат вычислений: {r:.3f}")


