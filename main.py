import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

df = pd.read_csv("filteredStars.csv")

star_name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

fig = px.bar(x = star_name , y = mass )
fig.show()

fig2 = px.bar(x = star_name , y = radius)
fig2.show()

fig3 = px.bar(x = star_name , y = dist)
fig3.show()

fig4 = px.bar(x = star_name , y = gravity)
fig4.show()
