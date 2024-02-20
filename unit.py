__author__ = 'Denisova E.'

import math
import random
import numpy as np

def rnd_list_int(n, a, b):
	""" создаёт список из случайных целых значений в диапазоне (a, b) """
	a = [  random.randint(a, b) #выражение для вычисления элементов списка
       for i in range(n) #цикл повторяет выражение
       ]

	return a


def rnd_list_float(n, a, b):
	""" создаёт список из случайных вещественных значений в диапазоне (a, b) """
	a = [  random.uniform(float(a), float(b)) #выражение для вычисления элементов списка
       for i in range(n) #цикл повторяет выражение
       ]
	return a


def calc_result136(a: list):
	""" вычисляет выражение по формуле: sqrt(abs(a[i])) - a[i])^2"""
	r = 0.0
	for i in range (len(a)):
		r += (math.sqrt(abs(a[i])) - a[i])**2

	return r


def test_calc_result():
	assert(calc_result136([4, -1]) == 8)
	#округление round
	assert(round(calc_result136([-9, 25, 6]),3) == 556.606)
	assert(round(calc_result136([2.2, -3.4]), 3) == 28.012)


def count_members178(a: list):
	"""возвращает количество элементов в списке, удовлетворяющих условию ak < ((ak-1 - ak+1)/2)"""
	c = 0
	for i in range(1, len(a)-1):
		if a[i] < ((a[i-1] - a[i+1]) / 2):
			c += 1
	return c


def test_count_members():
	assert(count_members178([4, 1]) == 0)
	assert(count_members178([1, 8, 2, 1, 6]) == 1)
	assert(count_members178([100, 2, 50, 1, 20, 2]) == 2)


def summ334(a: int, b: int):
	""" вычисляет сумму по формуле: (j-i+1)/(i+j)
	 a и b - верхние границы i и j"""
	s = 0
	for i in range(1, a+1):
		for j in range(1, b+1):
			s += (j-i+1)/(i+j)
	return s


def rearrange_columns676(m: np.ndarray):
	# Размеры матрицы
	rows, cols = m.shape

	# Создание новой матрицы для перестановки столбцов
	new_matrix = np.zeros((rows, cols), dtype=int)

	# Перестановка столбцов
	for i in range(cols):
		new_matrix[:, i] = m[:, cols - i - 1]

	return new_matrix

def test_rearrange_columns():
	matrix1 = np.array([
    	[1, 2, 3],
    	[4, 5, 6], 
    	[7, 8, 9],
	])

	m1 = np.array([
    	[3, 2, 1],
    	[6, 5, 4],
    	[9, 8, 7],
	])
	new_matrix1 = rearrange_columns676(matrix1)
	assert(np.allclose(m1, new_matrix1))

	matrix2 = np.array([
    	[-5, 8, 4, 7],
    	[9, 7, -6, 82], 
	])

	m2 = np.array([
    	[7, 4, 8, -5],
    	[82, -6, 7, 9],
	])
	new_matrix2 = rearrange_columns676(matrix2)
	assert(np.allclose(m2, new_matrix2))

	matrix3 = np.array([
    	[85, 96],
    	[-9, 7], 
    	[75,-4],
    	[-96, -57],
	])

	m3 = np.array([
    	[96, 85],
    	[7, -9],
    	[-4, 75],
    	[-57, -96],
	])
	new_matrix3 = rearrange_columns676(matrix3)
	assert(np.allclose(m3, new_matrix3))

