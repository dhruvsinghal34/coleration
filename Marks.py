import csv
import plotly.express as px
import numpy as n

def getDataSource(dataPath):
    marks=[]
    day=[]
    with open("Student Marks vs Days Present.csv") as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            marks.append(float(row["Marks In Percentage"]))
            day.append(float(row["Days Present"]))
    return{
        "x":day,
        "y":marks
    }

def findCorrelation(dataSource):
   correlation=n.corrcoef(dataSource["x"],dataSource["y"])
   print(correlation[0,1])

def setup():
    path = "Student Marks vs Days Present.csv"
    dataSource=getDataSource(path)
    findCorrelation(dataSource)

setup()
