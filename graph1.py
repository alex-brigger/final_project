import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

df = pd.read_csv("generation_data.csv")

def frame1():
    num_types = df.value_counts('ENERGY SOURCE')
    num_types = num_types.drop('Total')
    return num_types

def plot1(frame):
    frame.plot.bar(color = "Yellow")
    plt.xlabel('Energy Types')
    plt.title(('Total Uses of Each Energy Source from 2001-2022'), fontsize = 24)
    plt.ylabel('Number of Occurences')
    plt.yticks(np.arange(0, 100000, step=20000))
    plt.tight_layout()


def main():
    graph_frame = frame1()
    plot1(graph_frame)
    plt.show()
if __name__ == "__main__":
    main()
