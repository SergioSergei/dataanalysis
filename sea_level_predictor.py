import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = np.arange(df["Year"].min(), 2051)
    ax.plot(years_all, res_all.intercept + res_all.slope * years_all, color="red")

    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    ax.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, color="green")

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    fig.savefig("sea_level_plot.png")
    return fig
