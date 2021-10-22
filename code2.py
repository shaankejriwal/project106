import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    Days_Present = []
    Marks_In_Percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row['Days Present']))
    return{
        "x" : Marks_In_Percentage,
        "y" : Days_Present
    }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between Marks In Percentage vs Days Present: ", correlation[0,1])

def setup():
    data_path = "dataset1.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()