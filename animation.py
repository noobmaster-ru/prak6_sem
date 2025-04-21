import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np
from constants import T0,TN,N0,EPS,STEP

# Чтение данных
df = pd.read_csv("data.csv")

# Инициализация графика
fig = plt.figure(figsize=(13, 7))
ax = fig.add_subplot(111, projection='3d')

# Установка пределов по осям
ax.set_xlim(min(df["Time"]), max(df["Time"]))
ax.set_ylim(min(df["y1"]), max(df["y1"]))
ax.set_zlim(min(df["y2"]), max(df["y2"]))

# Подписи осей
ax.set_xlabel("y1", fontsize=12, fontweight='bold', labelpad=15)
ax.set_ylabel("y2", fontsize=12, fontweight='bold', labelpad=15)
ax.set_zlabel("y3", fontsize=12, fontweight='bold', labelpad=15)

# Пустая линия, которую будем обновлять
line, = ax.plot([], [], [], color='blue', label='Trajectory')
point, = ax.plot([], [], [], 'ro')  # текущая точка

# Функция инициализации
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

# Функция обновления
def update(frame):
    x = df["Time"][:frame]
    y = df["y1"][:frame]
    z = df["y2"][:frame]
    line.set_data(x, y)
    line.set_3d_properties(z)
    point.set_data(x.iloc[-1:], y.iloc[-1:])
    point.set_3d_properties(z.iloc[-1:])
    return line, point

# Анимация
ani = FuncAnimation(fig, update, frames=len(df), init_func=init,
                    interval=5, blit=True)

# Добавим текст с константами в правый верхний угол графика
_step = (TN-T0)/N0
textstr = '\n'.join((
    r'$T_0=%.1f$' % T0,
    r'$T_N=%.1f$' % TN,
    r'$N=%d$' % N0,
    r'$\varepsilon=%.2f$' % EPS,
    r'$Step=%.4f$' % _step
))

# Параметры для рамки текста
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Добавим текст на 2D-плоскость (не 3D)
plt.gcf().text(0.9, 0.85, textstr, fontsize=12, bbox=props)

# Показываем график
plt.legend()
plt.tight_layout()
plt.show()