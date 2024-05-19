import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

period = 1.0
total_strokes = 1000

theta = np.linspace(-np.pi / 2, np.pi / 2, 100)
wavelength = np.linspace(400, 750, 2000)

Theta, Wavelength = np.meshgrid(theta, wavelength)

Intensity = np.sin(np.pi * total_strokes * period * np.sin(Theta) / Wavelength) ** 2 / \
            (np.sin(np.pi * period * np.sin(Theta) / Wavelength) ** 2)

colors = [(0.0, 'blue'), (0.5, 'green'), (0.8, 'yellow'), (1.0, 'red')]
cmap_wave = LinearSegmentedColormap.from_list('wave', colors)

norm = Normalize(vmin=wavelength.min(), vmax=wavelength.max())

fig2 = plt.figure(figsize=(12, 6))

# График с основным содержимым
ax1 = fig2.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(Theta, Wavelength, Intensity, cmap='plasma')
ax1.set_xlabel('Угол дифракции')
ax1.set_ylabel('Длина волны, нм')
ax1.set_zlabel('Интенсивность')

# Создание отдельного графика для цветовой шкалы
ax2 = fig2.add_axes([0.91, 0.1, 0.02, 0.8])
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap_wave), cax=ax2)
cbar.set_label('Длина волны, нм')

plt.tight_layout()
plt.show()