e_charge = 1.60217662e-19 - заряд злектрона  -1,602176634 * 10^19 [Кл]

В данном случае берем абсолютное значение для более простых вичислений и наглядных графиков

m_electron = 9.10938356e-31  - масса электрона [Кг]

mu_0 = 4 * np.pi * 1e-7  - магнитная проницаемость вакуума [Гн/м]

---

````
def electron_motion(y, t, U, B, m, e):
    x, y, vx, vy = y
    dvxdt = (e / m) * vy * B
    dvydt = -(e / m) * vx * B - (e / m) * U * vy / np.sqrt(vx ** 2 + vy ** 2)
    return [vx, vy, dvxdt, dvydt]
````

1) sol = odeint(electron_motion, [x0, y0, v0, 0], t, args=(U, B, m_electron, e_charge))

       x, y, vx, vy = y y - [x0, y0, v0, 0]


2) dvxdt = (e / m) * vy * B  - это уравнение Лоренца, которое описывает силу, действующую на заряженную частицу, движущуюся в магнитном поле. 
    
       F_лоренца = q * v * B * sin(a), q - заряд, v - скорость, B вектор магнитной индукции, а - улог между v и B. У нас sin(a) = 1.
    
       По 2 З.Н. ∑F = ma, F = ma, F = q v B sin(a) => ma = q v B sin(a) => a = q/m v B sin(a), который у нас 1, тк V | B.  


3) dvydt = -(e / m) * vx * B - (e / m) * U * vy / np.sqrt(vx ** 2 + vy ** 2) 

       Минусы тут - направление, по поводу остального: (e / m) * vx * B - ну это уже понятно из п.2. 

       А (e / m) * U * vy / np.sqrt(vx ** 2 + vy ** 2) как я пон идет из E = F/q и qEd = qU.

       F = ma (II З.Н),
       F = Eq, F = ma => ma = Eq => a = (q/m)E ==(E = U/d)> a = (q/m)U/d, 

       как я пон по Пифагору нашли расстояние d => (np.sqrt(vx ** 2 + vy ** 2)) => (e / m) * U / np.sqrt(vx ** 2 + vy ** 2). vy тут скорее всего, чтобы учесть скорость (выводя это руками я не смог найти что-то с v).

---

````
def orbit_radius(I, D, n):
    B = mu_0 * n * I
    
    if B == 0:
        return
        
    return (m_electron * (D / 2) ** 2) / (2 * e_charge * B)
````

1) B = mu_0 * n * I 
    
       B - магнитное поле внутри соленоида,
    
       mu_0 - магнитная проницаемость вакуума,

       n - число витков на единицу длины соленоида,
   
       I - ток через соленоид.

    Это уже готовая формула 

    <p align="center">
    <img width="382" src="images/B.png" alt="qr"/>
    </p>

    [формула со studfile](https://studfile.net/preview/2953066/page:5/)

2) math.sqrt((m_electron * 2 * U)/(e_charge * (B ** 2)))
     
   уф, ну поехали

          F_центробежная = m w^2 r, где
          m - масса,
          w (омега) - угловая скорость,
          r - радиус.

   F_лоренца (была выше) = qvBsin(a) 
   
   ### вывод

           F_ц = F_л
        
           Когда заряженная частица движется в магнитном поле, на нее действует сила Лоренца.
           Если частица движется перпендикулярно магнитному полю, эта сила вызывает центробежное движение, и частица начинает двигаться по круговой орбите.

           mw^2r = qvBsin(a)                           (sin(a) = 1, v = wr => w = v/r)

           m (v/r)^2 r = qvB                           ((v/r)^2 * r/v = v/r)

           m v/r = qB                                  (умножаем на r делим на qB)

           mv/qB = r                                   (v = sqrt( 2 * e/m * U), q = e)

           m * sqrt(2 *  e/m * U) / e B = r            (m = sqrt(m^2) и тд)

           sqrt(m^2 * 2 * e/m * U / (e^2 * B^2)) = r   (сокращаем m и e)

           sqrt(m * 2 * U / (e * B^2)) = r

   ##### букОвы:
          
           F_ц - центробежная сила [Н],
           m - масса [Кг],
           w (омега) - угловая скорость [рад/с],
           r - радиус [м],
           F_л - сила Лоренца [H],
           B - вектор магнитной индукции [Тл],
           q - заряд [Кл],
           v - скорость [м/с],
           e - заряд электрона [Кл],
           U - напрядение [В].

   ##### формула для v

    <p align="center">
    <img width="382" src="images/v.png" alt="qr"/>
    </p>

   [формула со studfile](https://studfile.net/preview/1644348/)
---

````
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
````

1) n = 100  - Число витков на единицу длины, B = mu_0 * n * Ic  - Магнитное поле внутри соленоида (было разобрано в прошлом пункте)

2)  x0 = Rk, y0 = 0, v0 = np.sqrt(2 * e_charge * U / m_electron), r_orbit = orbit_radius(Ic, U, n)
   
   x0 = Rk    (Rk - радиус катода)

         Это начальное положение электрона по оси x.
         Электрон начинает свое движение из катода, поэтому его начальное положение по оси x равно радиусу катода

   y0 = 0
         
         Это начальное положение электрона по оси y.
         Поскольку мы рассматриваем движение электрона в плоскости x-y, мы можем считать, что электрон начинает свое движение из точки (Rk, 0)

   v0 = np.sqrt(2 * e_charge * U / m_electron)

         Это начальная скорость электрона.
   <p align="center">
    <img width="382" src="images/v.png" alt="qr"/>
    </p>

   [формула со studfile](https://studfile.net/preview/1644348/)

   r_orbit = orbit_radius(Ic, U, n)

         Вычисление радиуса орбиты через функцию из прошлого раздела.
         Тут Ic - ток в соленоиде [A], U - разность потенциалов/напряжение [B], n - число витков на единицу длины.

3) omega = v0 / r_orbit

   вот формула: 

   <p align="center">
    <img width="382" src="images/w.png" alt="qr"/>
    </p>

   Просто делим это на R
---