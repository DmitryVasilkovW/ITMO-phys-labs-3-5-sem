import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Исходные данные
x1 = np.array([3300, 2750, 2420, 2090, 1650, 1320, 880, 836, 704, 594, 484, 264, 253, 140.8, 33])
y1 = np.array([10.272, 11.916, 12.140, 11.353, 11.642, 10.272, 7.704, 6.488, 5.136, 4.565, 3.735, 4.280, 2.680, 2.568, 1.712])

# Вычисляем коэффициенты полиномиальной регрессии
coeff1 = np.polyfit(x1, y1, 6)

# Создаем полином с полученными коэффициентами
p1 = Polynomial(coeff1[::-1])


print("Полином для верхней части:", p1, "\n")
