import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

df = pd.read_csv("generation_data.csv")

def frame3():
    graph3 = df.loc[:,["YEAR", "ENERGY SOURCE", "GENERATION (Megawatthours)"]]
    ff = ["Coal", "Natural Gas", "Petroleum"]
    rslt_df = graph3.loc[df['ENERGY SOURCE'].isin(ff)]
    result = rslt_df.groupby(['YEAR']).agg({'GENERATION (Megawatthours)': sum}).drop(2022)
    return result


def plot3():
    years = np.array(range(2001,2022))
    frame_run = frame3()
    production = np.array(frame_run["GENERATION (Megawatthours)"])
    plt.scatter(years, production, label = 'Total Generation Per Year')
    plt.ylabel(("Fossil Fuel Usage"),fontsize = 20)
    plt.xlabel("Year")
    plt.title("Total Power Production Of Fossil Fuels Each Year")
    a, b = np.polyfit(years, production, 1)
    plt.plot(years, a*years+b)        
    plt.show()


def main():
    plot3()
    plt.show()
if __name__ == "__main__":
    main()