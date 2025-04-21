import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # подключение 3D-инструментов

# # Загружаем данные
# data = np.loadtxt("output.csv", delimiter=",")

# # Настройки
# points_per_curve = 100
# num_curves = len(data) // points_per_curve

# # Создаём 3D-график
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111, projection='3d')

# # Для каждой кривой рисуем линию
# for i in range(num_curves):
#     segment = data[i * points_per_curve : (i + 1) * points_per_curve]
#     t = segment[:, 0]
#     y1 = segment[:, 1]
#     y2 = segment[:, 2]
    
#     ax.plot3D(t, y1, y2, label=f'Кривая {i+1}')  # линия в 3D

# # Подписи осей
# ax.set_xlabel("t")
# ax.set_ylabel("y1")
# ax.set_zlabel("y2")
# ax.set_title("3D-график: t, y1, y2")
# plt.legend()
# plt.tight_layout()
# plt.show()
# print(plt.style.available)


# Чтение данных
df = pd.read_csv("data.csv")

# Инициализация 3D-графика
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Вытаскиваем начальную и конечную точки
start = df.iloc[0]
end = df.iloc[-1]

#  Точки начала и конца
ax.scatter([start["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=50, label="Start", zorder=5)
ax.scatter([end["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=50, label="End", zorder=5)


# # --- Проекции начальной точки ---
# # на плоскость y1-y2
# ax.plot([0,start["Time"]],[start["y1"], start["y1"]], [start["y2"], start["y2"]], [0, start["y3"]], color='green', linestyle='dashed')
# # на плоскость y1-y3
# ax.plot([0,start["Time"]],[start["y1"], start["y1"]], [0, start["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
# # на плоскость y2-y3
# ax.plot([0,start["Time"]],[0, start["y1"]], [start["y2"], start["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')


# Построение траектории в пространстве y1, y2, y3
ax.plot(df["Time"],df["y1"], df["y2"], df["y3"], label="Trajectory", color="blue",linewidth=2)


# Настройка подписей
ax.set_xlabel("y1")
ax.set_ylabel("y2")
ax.set_zlabel("y3")



ax.set_xlabel("y1", fontsize=12)
ax.set_ylabel("y2", fontsize=12)
ax.set_zlabel("y3", fontsize=12)
ax.set_title("3D Trajectory in State Space", fontsize=14)

# Добавление легенды и сетки
ax.legend()
ax.view_init(elev=40, azim=140)
ax.grid(True)

# Показ графика
plt.tight_layout()
plt.show()