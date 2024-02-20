__author__ = 'Denisova E.'
#Дана целочисленная матрица размера 6х9. Найти матрицу получающуюся из данной:
#a) перестановкой столбцов - первого с последним, второго с предпоследним и т.д.
import numpy as np
import unit

unit.test_rearrange_columns()

# Исходная матрица размера 6x9
matrix = np.random.randint(1, 100, size=(6, 9))

print(type(matrix))

new_matrix = unit.rearrange_columns676(matrix)

# Вывод исходной и полученной матрицы
print("Исходная матрица:\n", matrix)
print("\nМатрица после перестановки столбцов:\n", new_matrix)
