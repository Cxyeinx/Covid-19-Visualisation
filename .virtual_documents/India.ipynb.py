import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")


df = pd.read_csv("covid_19_india.csv")
df["Date"] = pd.to_datetime(df["Date"])


df.head()


dates = sorted(set(df["Date"]))


new_df = {}


for date in dates:
    new_df[date] = [sum(df[df["Date"] == date]["Confirmed"].values.tolist()), sum(df[df["Date"] == date]["Deaths"].values.tolist()), sum(df[df["Date"] == date]["Cured"].values.tolist())]


date = np.array(list(new_df.keys()))
confirmed = np.array(list(i[0] for i in new_df.values()))
deaths = np.array(list(i[1] for i in new_df.values()))
cured = np.array(list(i[2] for i in new_df.values()))


fig, ax = plt.subplots()  # a figure with a single Axes
ax.plot(date, cured, color="g")
ax.plot(date, deaths, color="r")
ax.plot(date, confirmed, color="b")
ax.ticklabel_format(style='plain', axis='y')
ax.legend(["Cured", "Deaths", "Confirmed"])
plt.xticks(rotation=30)
plt.xlabel("Dates")
plt.ylabel("Number of People")
plt.title("Total Cases in India from March 2020 to May 2021")
plt.show()
fig.savefig("india.png")



