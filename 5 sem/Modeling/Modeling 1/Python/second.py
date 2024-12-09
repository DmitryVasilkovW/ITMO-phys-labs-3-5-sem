import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def a_b():
    def U(x):
        U0 = 5e-20
        sigma = 0.5e-9
        return U0 * np.exp(-x ** 2 / (2 * sigma ** 2))

    E = 4.5e-20
    m = 9.1e-31
    hbar = 1.054e-34

    def k(x):
        return np.sqrt(2 * m * (U(x) - E)) / hbar if U(x) > E else 0

    x = np.linspace(-2e-9, 2e-9, 1000)
    x1 = x[np.argmax(U(x) > E)]
    x2 = x[::-1][np.argmax(U(x[::-1]) > E)]

    integral, _ = quad(k, x1, x2)
    T = np.exp(-2 * integral)

    print(f"Вероятность туннелирования: T = {round(T, 2)}")

    plt.figure(figsize=(8, 5))
    plt.plot(x, U(x), label="$U(x)$", color="black")
    plt.axhline(E, color="red", linestyle="--", label="$E$")
    plt.title("Прохождение частицы через потенциальный барьер")
    plt.xlabel("$x$, м")
    plt.ylabel("$U$, Дж")
    plt.legend()
    plt.grid()
    plt.show()
