import plotly.express as px
import csv

with open ("Student Marks vs Days Present.csv") as csv_File:
    df = csv.DictReader(csv_File)
    fig = px.scatter(df,x="Roll No",y="Marks In Percentage",color="Days Present")
    fig.show()