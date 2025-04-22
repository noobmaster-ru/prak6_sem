import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # подключение 3D-инструментов
import time
from constants import T0,TN,N0,EPS,STEP,D,M,NUM_TRAJECTORY
# Чтение данных
df = pd.read_csv("data.csv")

# Находим индексы, где Time == 0 (начало каждой кривой)
start_indices = df.index[df["Time"] == 0].tolist()

# Добавим "конец" тоже
start_indices.append(len(df))


# Инициализация 3D-графика
fig = plt.figure(figsize=(14, 7.5))
ax = fig.add_subplot(111, projection='3d')

# Разные цвета для каждой траектории
colors = ["blue", "red", "green", "orange", "purple"]


for i in range(len(start_indices) - 1):
    start_index = start_indices[i]
    end_index = start_indices[i + 1] 
    curve = df.iloc[start_index:end_index]
    print(curve)
    # Вытаскиваем начальную и конечную точки
    start = df.iloc[start_index]
    end = df.iloc[end_index]

    #  Точки начала и конца
    ax.scatter([start["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=60, label="Начальная точка", zorder=5)
    ax.scatter([end["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=60, label="Конечная точка", zorder=5)


    # # --- Проекции начальной точки ---
    # # на плоскость y2-y3
    ax.plot([start["Time"],end["Time"]],[start["y1"], start["y1"]], [start["y2"], start["y2"]], [end["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([end["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=10, zorder=5)
    # на плоскость y1-y2
    ax.plot([start["Time"],start["Time"]],[start["y1"], start["y1"]], [start["y2"], end["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([start["Time"]],[start["y1"]], [end["y2"]], [start["y3"]], color="green", s=10, zorder=5)
    # # на плоскость y1-y3
    ax.plot([start["Time"],start["Time"]],[end["y1"], start["y1"]], [start["y2"], start["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([start["Time"]],[end["y1"]], [start["y2"]], [start["y3"]], color="green", s=10, zorder=5)

    # --- Проекции конечной точки ---
    # # на плоскость y2-y3
    ax.plot([end["Time"],start["Time"]],[end["y1"], end["y1"]], [end["y2"], end["y2"]], [start["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([start["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=10, zorder=5)
    # на плоскость y1-y2
    ax.plot([end["Time"],end["Time"]],[end["y1"], end["y1"]], [end["y2"], start["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([end["Time"]],[end["y1"]], [start["y2"]], [end["y3"]], color="red", s=10, zorder=5)
    # # на плоскость y1-y3
    ax.plot([end["Time"],end["Time"]],[start["y1"], end["y1"]], [end["y2"], end["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([end["Time"]],[start["y1"]], [end["y2"]], [end["y3"]], color="red", s=10, zorder=5)


    # Построение траектории в пространстве y1, y2, y3
    ax.plot(curve["Time"],curve["y1"], curve["y2"], curve["y3"], label=f"Кривая {i+1}", color=colors[i])
    # Построение траектории в пространстве y1, y2, y3 - старое
    # ax.plot(df["Time"],df["y1"], df["y2"], df["y3"], label="Траектория", color="blue",linewidth=3)


ax.set_xlabel("y1", labelpad=20, fontsize=12)
ax.set_ylabel("y2", labelpad=20, fontsize=12)
ax.set_zlabel("y3", labelpad=20, fontsize=12)
ax.set_title("График решения", fontsize=16)

# Добавление легенды и сетки
ax.legend(loc='best')
ax.view_init(elev=40, azim=140)
ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys())

# Добавим текст с константами в правый верхний угол графика
_step = (TN-T0)/N0
textstr = '\n'.join((
    r'$D=%s$' % f"{D} - {D + NUM_TRAJECTORY*0.05}",
    r'$M=%.2f$' % M,
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
plt.savefig(f"pig_{time.time()}.jpg")
# Показ графика
plt.tight_layout()
plt.show()