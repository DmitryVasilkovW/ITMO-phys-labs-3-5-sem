import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize
from mpl_toolkits.mplot3d import Axes3D

period = 1.0
total_strokes = 1000

theta = np.linspace(-np.pi / 2, np.pi / 2, 100)
wavelength = np.linspace(450, 495, 2000)  # Измените эту строку

Theta, Wavelength = np.meshgrid(theta, wavelength)

# Выберите длину волны для синего цвета (около 470 нм)
blue_wavelength = 470

# Вычислите интенсивность для этой длины волны
Intensity_blue = np.sin(np.pi * total_strokes * period * np.sin(Theta) / blue_wavelength) ** 2 / \
            (np.sin(np.pi * period * np.sin(Theta) / blue_wavelength) ** 2)

# Создайте новый график
fig3 = plt.figure(figsize=(6, 6))
ax3 = fig3.add_subplot(111, projection='3d')

# Создайте пользовательскую цветовую карту от голубого до черного с большим количеством точек для плавного перехода
colors_blue = [(0.0, 'blue'), (0.5, 'blue'), (0.75, 'darkblue'), (1.0, 'black')]
cmap_blue = LinearSegmentedColormap.from_list('blue', colors_blue)

# Нормализуйте интенсивность для использования в качестве цветового отображения
norm_intensity = Normalize(vmin=Intensity_blue.min(), vmax=Intensity_blue.max())

# Создайте поверхность с использованием интенсивности в качестве цветового отображения
surf2 = ax3.plot_surface(Theta, Wavelength, Intensity_blue, facecolors=cmap_blue(norm_intensity(Intensity_blue)))

ax3.set_xlabel('Угол дифракции')
ax3.set_ylabel('Длина волны, нм')
ax3.set_zlabel('Интенсивность')

plt.tight_layout()
plt.show()
