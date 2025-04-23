import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # connect 3D-tools
import time
from constants import T0,TN,N0,EPS,D,M,FILENAME
import matplotlib.gridspec as gridspec


def make_3d_plot(df):
    # Starting and ending points
    start = df.iloc[0]
    end = df.iloc[-1]

    # Drow the start and end points
    ax.scatter([start["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=10, label="Begin point", zorder=5)
    ax.scatter([end["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=10, label="End point", zorder=5)


    #  --- Projections start point ---
    # for y2-y3
    ax.plot([start["Time"],end["Time"]],[start["y1"], start["y1"]], [start["y2"], start["y2"]], [end["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([end["Time"]],[start["y1"]], [start["y2"]], [start["y3"]], color="green", s=5, zorder=5)
    # for y1-y2
    ax.plot([start["Time"],start["Time"]],[start["y1"], start["y1"]], [start["y2"], end["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([start["Time"]],[start["y1"]], [end["y2"]], [start["y3"]], color="green", s=5, zorder=5)
    # for y1-y3
    ax.plot([start["Time"],start["Time"]],[end["y1"], start["y1"]], [start["y2"], start["y2"]], [start["y3"], start["y3"]], color='green', linestyle='dashed')
    ax.scatter([start["Time"]],[end["y1"]], [start["y2"]], [start["y3"]], color="green", s=5, zorder=5)

    # --- Projections end point ---
    # for  y2-y3
    ax.plot([end["Time"],start["Time"]],[end["y1"], end["y1"]], [end["y2"], end["y2"]], [start["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([start["Time"]],[end["y1"]], [end["y2"]], [end["y3"]], color="red", s=5, zorder=5)
    # for y1-y2
    ax.plot([end["Time"],end["Time"]],[end["y1"], end["y1"]], [end["y2"], start["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([end["Time"]],[end["y1"]], [start["y2"]], [end["y3"]], color="red", s=5, zorder=5)
    # for y1-y3
    ax.plot([end["Time"],end["Time"]],[start["y1"], end["y1"]], [end["y2"], end["y2"]], [end["y3"], end["y3"]], color='red', linestyle='dashed')
    ax.scatter([end["Time"]],[start["y1"]], [end["y2"]], [end["y3"]], color="red", s=5, zorder=5)


    # Make trajectory for y1, y2, y3
    ax.plot(df["Time"],df["y1"], df["y2"], df["y3"], label="Trajectory", color="blue",linewidth=1.5)

    ax.set_xlabel("Y1", labelpad=25, fontsize=14,fontweight='bold')
    ax.set_ylabel("Y2", labelpad=25, fontsize=14,fontweight='bold')
    ax.set_zlabel("Y3", labelpad=25, fontsize=14,fontweight='bold')
    ax.set_title("Plot of solution", fontsize=20)

    # Add legend and grid
    ax.legend(loc='best')  
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
    # Read dataframe
    print("Open datas/data0.csv")
    df = pd.read_csv("datas/data0.csv")

    # Init 3D-plot
    fig = plt.figure(figsize=(15, 7.5))
    gs = gridspec.GridSpec(3, 2, width_ratios=[2, 1]) # 3 rows ,2 columns

    ax = fig.add_subplot(gs[:, 0], projection='3d')

    make_3d_plot(df)
    make_2d_plot(df, "y1", gs[0, 1])
    make_2d_plot(df, "y2", gs[1, 1])
    make_2d_plot(df, "y3", gs[2, 1])


    #  Add text with constants to the left upper corner
    _step = (TN-T0)/N0
    textstr = '\n'.join((
        r'$D=%.2f$' % D,
        r'$M=%.2f$' % M,
        r'$T_0=%.1f$' % T0,
        r'$T_N=%.1f$' % TN,
        r'$N=%d$' % N0,
        r'$\varepsilon=%.3f$' % EPS,
        r'$Step=%.3f$' % _step
    ))
    props = dict(boxstyle='round', facecolor='white', alpha=0.5) 


    plt.gcf().text(0.01, 0.79, textstr, fontsize=11, bbox=props)
    plt.savefig(f"pictures/pig_{time.time()}.jpg")
    # Show plot
    plt.tight_layout()
    plt.show()