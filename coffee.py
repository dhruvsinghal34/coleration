import csv
import plotly.express as px
import numpy as n

def getDataSource(dataPath):
    coffeeCups=[]
    sleep=[]
    with open("cups of coffee vs hours of sleep.csv") as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            coffeeCups.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{
        "x":coffeeCups,
       "y":sleep
    }

def findCorrelation(dataSource):
   correlation=n.corrcoef(dataSource["x"],dataSource["y"])
   print(correlation[0,1])

def setup():
    path = "cups of coffee vs hours of sleep.csv"
    dataSource=getDataSource(path)
    findCorrelation(dataSource)

setup()




