import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # подключение 3D-инструментов

# Чтение данных
df = pd.read_csv("output.csv")

# Инициализация 3D-графика
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Построение траектории в пространстве y1, y2, y3
ax.plot(df["Time"],df["y1"], df["y2"], df["y3"], label="Trajectory", color="blue")

# Настройка подписей
ax.set_xlabel("y1")
ax.set_ylabel("y2")
ax.set_zlabel("y3")
# ax.set_title("3D Trajectory in State Space")

# Добавление легенды и сетки
ax.legend()

ax.grid(True)

# Показ графика
plt.show()