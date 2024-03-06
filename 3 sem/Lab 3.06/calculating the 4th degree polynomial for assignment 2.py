import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Исходные данные
x1 = np.array([2, 1, 0.5, 0, -0.7, -1.2, -1.9, -2.8])
y1 = np.array([3, 2.5, 2, 1.5, 0, -1, -2, -3])

x2 = np.array([2.8, 2, 1.6, 1.4, 1, 0.8, 0, -0.5, -1, -2, -3])
y2 = np.array([3, 2.2, 2, 1, 1.8, 0, -1.4, -2, -2.3, -2.9, -3.1])

# Вычисляем коэффициенты полиномиальной регрессии
coeff1 = np.polyfit(x1, y1, 4)
coeff2 = np.polyfit(x2, y2, 4)

# Создаем полином с полученными коэффициентами
p1 = Polynomial(coeff1[::-1])
p2 = Polynomial(coeff2[::-1])


print("Полином для верхней части:", p1, "\n")
print("Полином для нижней части:", p2, "\n")
