import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

period = 1.0
total_strokes = 1000
d = 3

theta = np.linspace(-np.pi / 2, np.pi / 2, 100)
wavelength = np.linspace(400, 750, 2000)

Theta, Wavelength = np.meshgrid(theta, wavelength)

Intensity = np.sin(np.pi * period * np.sin(Theta) / Wavelength) ** 2 / \
            ((np.pi * period * np.sin(Theta) / Wavelength) ** 2)

tmp = np.sin(np.pi * total_strokes * d * np.sin(Theta) / Wavelength) ** 2 / \
            np.sin(np.pi * d * np.sin(Theta) / Wavelength) ** 2

Intensity *= tmp


colors = [(0.0, 'violet'), (0.15, 'indigo'), (0.3, 'blue'),
          (0.45, 'green'), (0.6, 'yellow'),
          (0.75, 'orange'), (1.0, 'red')]
cmap_wave = LinearSegmentedColormap.from_list('wave', colors)

norm = Normalize(vmin=wavelength.min(), vmax=wavelength.max())

fig2 = plt.figure(figsize=(12, 6))

ax1 = fig2.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(Theta, Wavelength, Intensity, facecolors=cmap_wave(norm(Wavelength)))
ax1.set_xlabel('Угол дифракции')
ax1.set_ylabel('Длина волны, нм')
ax1.set_zlabel('Интенсивность')

ax2 = fig2.add_axes([0.91, 0.1, 0.02, 0.8])
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap_wave), cax=ax2)
cbar.set_label('Длина волны, нм')

plt.tight_layout()
plt.show()

wavelength = np.linspace(450, 495, 2000)
Theta, Wavelength = np.meshgrid(theta, wavelength)

blue_wavelength = 470

Intensity_blue = np.sin(np.pi * period * np.sin(Theta) / blue_wavelength) ** 2 / \
            ((np.pi * period * np.sin(Theta) / blue_wavelength) ** 2)

tmp = np.sin(np.pi * total_strokes * d * np.sin(Theta) / blue_wavelength) ** 2 / \
            np.sin(np.pi * d * np.sin(Theta) / blue_wavelength) ** 2

Intensity_blue *= tmp

fig3 = plt.figure(figsize=(6, 6))
ax3 = fig3.add_subplot(111, projection='3d')

colors_blue = [(0.0, 'blue'), (0.5, 'blue'), (0.75, 'darkblue'), (1.0, 'black')]
cmap_blue = LinearSegmentedColormap.from_list('blue', colors_blue)

norm_intensity = Normalize(vmin=Intensity_blue.min(), vmax=Intensity_blue.max())

surf2 = ax3.plot_surface(Theta, Wavelength, Intensity_blue, facecolors=cmap_blue(norm_intensity(Intensity_blue)))

ax3.set_xlabel('Угол дифракции')
ax3.set_ylabel('Длина волны, нм')
ax3.set_zlabel('Интенсивность')

plt.tight_layout()
plt.show()