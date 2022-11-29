import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("generation_data.csv")

def frame1():
    num_types = df.value_counts('ENERGY SOURCE')
    num_types = num_types.drop('Total')
    return num_types

def plot1(frame):
    plt.xlabel('Energy Types')
    plt.title('Total Uses of Each Energy Source from 2001-2022')
    plt.ylabel('Number of Occurences')
    frame.plot.bar()


def main():
    graph_frame = frame1()
    plot1(graph_frame)
    plt.show()
    
if __name__ == "__main__":
    main()