import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Константы
e_charge = 1.60217662e-19  # элементарный заряд
m_electron = 9.10938356e-31  # масса электрона
mu_0 = 4 * np.pi * 1e-7  # магнитная проницаемость вакуума


# Функция для дифференциальных уравнений, описывающих движение электрона
def electron_motion(y, t, U, B, m, e):
    x, y, vx, vy = y
    dvxdt = (e / m) * vy * B
    dvydt = -(e / m) * vx * B - (e / m) * U * vy / np.sqrt(vx ** 2 + vy ** 2)

    return [vx, vy, dvxdt, dvydt]


# Функция для вычисления радиуса орбиты электрона
def orbit_radius(I, U, n):
    B = mu_0 * n * I

    if B == 0:
        return

    return math.sqrt((m_electron * 2 * U)/(e_charge * (B ** 2)))


def simulate_and_plot(U, Ic, Rk, steps=1000, tmax=1e-6, stop_velocity=None):
    n = 100  # Число витков на единицу длины
    B = mu_0 * n * Ic  # Магнитное поле внутри соленоида

    # Начальные условия
    x0 = Rk
    y0 = 0
    v0 = np.sqrt(2 * e_charge * U / m_electron)
    r_orbit = orbit_radius(Ic, U, n)  # Вычисление радиуса орбиты

    # Угловая скорость электрона
    omega = v0 / r_orbit

    # Временной массив
    t = np.linspace(0, tmax, steps)

    # Решение дифференциальных уравнений
    sol = odeint(electron_motion, [x0, y0, v0, 0], t, args=(U, B, m_electron, e_charge))

    # Остановка моделирования по заданной скорости
    if stop_velocity is not None:
        idx = np.where(np.sqrt(sol[:, 2] ** 2 + sol[:, 3] ** 2) <= stop_velocity)[0]
        if len(idx) > 0:
            sol = sol[:idx[0] + 1]

    # Построение траектории
    plt.figure(figsize=(8, 6))
    plt.plot(sol[:, 0], sol[:, 1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Траектория электрона')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

    return r_orbit


def find_required_current(D, Ra, Rk, n, I):
    r_orbit = (Ra - Rk) / 2  # Радиус окружности

    if (2 * e_charge * mu_0 * n * r_orbit * I) == 0:
        return

    Ic_required = (m_electron * (D / 2) ** 2) / (2 * e_charge * mu_0 * n * r_orbit * I)

    return Ic_required


# Функция для построения диаграммы (Ic от U) и отметки области, где электрон описывает окружность диаметром (Ra-Rk)
def plot_Ic_U_diagram_with_circle(D, Ra, Rk, n):
    U_values = np.linspace(0, 1000, 100)  # Диапазон разности потенциалов

    # Создание списка для значений силы тока в соленоиде
    Ic_values = []

    for U in U_values:
        # Вычисление соответствующей силы тока Ic, чтобы электрон описывал окружность диаметром (Ra-Rk)
        Ic_required = find_required_current(D, Ra, Rk, n, U)
        Ic_values.append(Ic_required)

    # Приведение значений к числовому типу
    Ic_values = np.array(Ic_values, dtype=np.float64)

    plt.figure(figsize=(8, 6))
    plt.plot(U_values, Ic_values, label='Ic', color='blue')

    plt.fill_between(U_values, Ic_values, color='red', alpha=0.3, label='Электрон описывает окружность (Ra-Rk)')

    plt.xlabel('Разность потенциалов (U)')
    plt.ylabel('Сила тока в соленоиде (Ic)')
    plt.title('Диаграмма Ic от U')
    plt.grid(True)
    plt.legend()
    plt.show()


# Пример использования
D = 0.1  # Диаметр соленоида в метрах
Ra = 0.01  # Радиус анода в метрах
Rk = 0.005  # Радиус катода в метрах
U = 100  # Разность потенциалов в вольтах
Ic = 1  # Начальное значение тока в соленоиде
n = 100  # Число витков на единицу длины

# Моделирование и построение траектории
r_orbit = simulate_and_plot(U, Ic, Rk, stop_velocity=1e5)
print("Радиус орбиты электрона:", r_orbit)

# Построение диаграммы Ic от U
plot_Ic_U_diagram_with_circle(D, Ra, Rk, n)