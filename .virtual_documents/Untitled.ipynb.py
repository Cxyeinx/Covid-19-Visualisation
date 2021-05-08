import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")


df = pd.read_csv("covid_19_india.csv")


df.head()


df["Date"] = pd.to_datetime(df["Date"])


cured = np.array(df[df["State/UnionTerritory"] == "Maharashtra"]["Cured"])
deaths = np.array(df[df["State/UnionTerritory"] == "Maharashtra"]["Deaths"])
confirmed = np.array(df[df["State/UnionTerritory"] == "Maharashtra"]["Confirmed"])
date = np.array(df[df["State/UnionTerritory"] == "Maharashtra"]["Date"])


fig, ax = plt.subplots()  # a figure with a single Axes
ax.plot(date, cured, color="g")
ax.plot(date, deaths, color="r")
ax.plot(date, confirmed, color="b")
ax.ticklabel_format(style='plain', axis='y')
ax.legend(["Cured", "Deaths", "Confirmed"])
plt.xticks(rotation=30)
plt.xlabel("Dates")
plt.ylabel("Number of People")
plt.title("Total Cases in Maharashtra from March 2020 to May 2021")
plt.show()
fig.savefig("Maharashtra.png")



