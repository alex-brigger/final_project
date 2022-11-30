import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def frame2():
    df = pd.read_csv("generation_data.csv")
    df21 = df.query("YEAR == 2021" or "YEAR == 2010" or "YEAR == 2011")
    return df21.groupby(['STATE']).agg({'GENERATION (Megawatthours)': sum}).drop('US-TOTAL').sort_values(by='GENERATION (Megawatthours)', ascending=False).head(5)

def plot2(frame2):
    frame2.plot.bar()
    plt.xlabel('States')
    plt.title('Top 5 Energy Producing States in 2021')
    plt.ylabel('Megawatt Hours Produced')
    plt.legend("Energy Generated in Megawatt Hours")
    

def main():
    graph_frame2 = frame2()
    plot2(graph_frame2)
    plt.show()
if __name__ == "__main__":
    main()