import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    sleep_in_hours = []
    Coffee_in_ml = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["\tsleep in hours"]))
    return{
        "x" : Coffee_in_ml,
        "y" : sleep_in_hours
    }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between Coffee in ml vs sleep in hours is : ", correlation[0,1])

def setup():
    data_path = "dataset2.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()