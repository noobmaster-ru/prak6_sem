import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # подключение 3D-инструментов

# Чтение данных
df = pd.read_csv("data.csv")

# Инициализация 3D-графика
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')



# Вытаскиваем начальную и конечную точки
start = df.iloc[0]
end = df.iloc[-1]

#  Точки начала и конца
ax.scatter([start["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=60, label="Start", zorder=5)
ax.scatter([end["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=60, label="End", zorder=5)


# # --- Проекции начальной точки ---
# # на плоскость y2-y3
ax.plot([start["Time"],end["Time"]],[start["y1"], start["y1"]], [start["y2"], start["y2"]], [end["y3"], start["y3"]], color='green', linestyle='dashed')
ax.scatter([end["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=25, zorder=5)
# на плоскость y1-y2
ax.plot([start["Time"],start["Time"]],[start["y1"], start["y1"]], [start["y2"], end["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
ax.scatter([start["Time"]],[start["y1"]], [end["y2"]], [start["y3"]], color="green", s=25, zorder=5)
# # на плоскость y1-y3
ax.plot([start["Time"],start["Time"]],[end["y1"], start["y1"]], [start["y2"], start["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
ax.scatter([start["Time"]],[end["y1"]], [start["y2"]], [start["y3"]], color="green", s=25, zorder=5)

# --- Проекции конечной точки ---
# # на плоскость y2-y3
ax.plot([end["Time"],start["Time"]],[end["y1"], end["y1"]], [end["y2"], end["y2"]], [start["y3"], end["y3"]], color='red', linestyle='dashed')
ax.scatter([start["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=25, zorder=5)
# на плоскость y1-y2
ax.plot([end["Time"],end["Time"]],[end["y1"], end["y1"]], [end["y2"], start["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
ax.scatter([end["Time"]],[end["y1"]], [start["y2"]], [end["y3"]], color="red", s=25, zorder=5)
# # на плоскость y1-y3
ax.plot([end["Time"],end["Time"]],[start["y1"], end["y1"]], [end["y2"], end["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
ax.scatter([end["Time"]],[start["y1"]], [end["y2"]], [end["y3"]], color="red", s=25, zorder=5)


# Построение траектории в пространстве y1, y2, y3
ax.plot(df["Time"],df["y1"], df["y2"], df["y3"], label="Trajectory", color="blue",linewidth=3)



ax.set_xlabel("y1", labelpad=20, fontsize=12)
ax.set_ylabel("y2", labelpad=20, fontsize=12)
ax.set_zlabel("y3", labelpad=20, fontsize=12)
ax.set_title("График решения", fontsize=16)

# Добавление легенды и сетки
ax.legend()
ax.view_init(elev=40, azim=140)
ax.grid(True)

# Показ графика
plt.tight_layout()
plt.show()