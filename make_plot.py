import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # подключение 3D-инструментов
import time
from constants import T0,TN,N0,EPS,STEP,D,M,NUM_TRAJECTORY
import matplotlib.gridspec as gridspec


def make_3d_plot(df):
    # Вытаскиваем начальную и конечную точки
    start = df.iloc[0]
    end = df.iloc[-1]

    #  Точки начала и конца
    ax.scatter([start["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=10, label="Начальная точка", zorder=5)
    ax.scatter([end["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=10, label="Конечная точка", zorder=5)


    # # --- Проекции начальной точки ---
    # # на плоскость y2-y3
    ax.plot([start["Time"],end["Time"]],[start["y1"], start["y1"]], [start["y2"], start["y2"]], [end["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([end["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=5, zorder=5)
    # на плоскость y1-y2
    ax.plot([start["Time"],start["Time"]],[start["y1"], start["y1"]], [start["y2"], end["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([start["Time"]],[start["y1"]], [end["y2"]], [start["y3"]], color="green", s=5, zorder=5)
    # # на плоскость y1-y3
    ax.plot([start["Time"],start["Time"]],[end["y1"], start["y1"]], [start["y2"], start["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([start["Time"]],[end["y1"]], [start["y2"]], [start["y3"]], color="green", s=5, zorder=5)

    # --- Проекции конечной точки ---
    # # на плоскость y2-y3
    ax.plot([end["Time"],start["Time"]],[end["y1"], end["y1"]], [end["y2"], end["y2"]], [start["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([start["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=5, zorder=5)
    # на плоскость y1-y2
    ax.plot([end["Time"],end["Time"]],[end["y1"], end["y1"]], [end["y2"], start["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([end["Time"]],[end["y1"]], [start["y2"]], [end["y3"]], color="red", s=5, zorder=5)
    # # на плоскость y1-y3
    ax.plot([end["Time"],end["Time"]],[start["y1"], end["y1"]], [end["y2"], end["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([end["Time"]],[start["y1"]], [end["y2"]], [end["y3"]], color="red", s=5, zorder=5)


    # Построение траектории в пространстве y1, y2, y3
    ax.plot(df["Time"],df["y1"], df["y2"], df["y3"], label="Траектория", color="blue",linewidth=1.5)

    ax.set_xlabel("Y1", labelpad=25, fontsize=14,fontweight='bold')
    ax.set_ylabel("Y2", labelpad=25, fontsize=14,fontweight='bold')
    ax.set_zlabel("Y3", labelpad=25, fontsize=14,fontweight='bold')
    ax.set_title("График решения системы", fontsize=20)

    # Добавление легенды и сетки
    ax.legend(loc='best')  # ax1 — это твой 3D-график    
    ax.view_init(elev=40, azim=140)
    ax.grid(True)

    handles, labels = ax.get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))
    ax.legend(unique_labels.values(), unique_labels.keys())


def make_2d_plot(df, column_name, position):
    ax2 = fig.add_subplot(position)
    ax2.plot(df["Time"], df[column_name], color='blue')
    ax2.set_xlabel("Time")
    ax2.set_ylabel(column_name.upper())
    ax2.grid(True)


if __name__ == "__main__":
    # Чтение данных
    df = pd.read_csv("data.csv")

    # Инициализация 3D-графика
    fig = plt.figure(figsize=(14, 8))
    gs = gridspec.GridSpec(3, 2, width_ratios=[2, 1])  # 3 строки, 2 столбца

    ax = fig.add_subplot(gs[:, 0], projection='3d')

    make_3d_plot(df)
    make_2d_plot(df, "y1", gs[0, 1])
    make_2d_plot(df, "y2", gs[1, 1])
    make_2d_plot(df, "y3", gs[2, 1])


    # Добавим текст с константами в правый верхний угол графика
    _step = (TN-T0)/N0
    textstr = '\n'.join((
        r'$D=%.2f$' % D,
        r'$M=%.2f$' % M,
        r'$T_0=%.1f$' % T0,
        r'$T_N=%.1f$' % TN,
        r'$N=%d$' % N0,
        r'$\varepsilon=%.3f$' % EPS,
        r'$Step=%.3f$' % _step,
        r'$NUM\_TRAJECTORY=%d$' % NUM_TRAJECTORY
    ))

    # Параметры для рамки текста
    props = dict(boxstyle='round', facecolor='white', alpha=0.5) # alpha - прозрачность

    # Добавим текст на 2D-плоскость (не 3D)
    plt.gcf().text(0.01, 0.8, textstr, fontsize=11, bbox=props)
    plt.savefig(f"pictures/pig_{time.time()}.jpg")
    # Показ графика
    plt.tight_layout()
    plt.show()