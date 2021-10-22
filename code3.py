import plotly.express as px
import csv
with open("dataset2.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Coffee in ml", y = "\tsleep in hours")
    fig.show()