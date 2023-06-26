from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import time
import json
import os
import math

window = Tk()
window.title("Health Tracker")
prediction = 0

def linear_reggression(a=[], b=[]):
    dates = []
    for x in a:
        date = x.split("-")
        date = (int(date[0])-1)*31 + int(date[1])
        dates.append(date)
        
    
    nor_dates = []
    for date in dates:
        date = date - (dates[0] -1)
        nor_dates.append(date)
    dates = nor_dates

    
    avg_dates = math.fsum(dates)/len(dates)
    avg_BSL = math.fsum(b)/len(b)
    dates_MAD = []
    BSL_MAD = []
    
    for date in dates:
        dates_MAD.append(date-avg_dates)
    for B in b:
        BSL_MAD.append(B-avg_BSL)
    slope_y = []
    
    for x in range(len(b)):
        slope_y.append(BSL_MAD[x] * BSL_MAD[x])
    dates_MAD_2 = [int(x)^2 for x in dates_MAD]
    slope = math.fsum(slope_y)/math.fsum(dates_MAD_2)
    
    y_int = avg_BSL/(avg_dates*slope)
    
    n_date = dates[-1]+1
   
    equation_line = slope*n_date + y_int
    
    return(equation_line)


def updatefun():
    global prediction

    try:
        with open("data.json", "r") as f: 
            pass
    except FileNotFoundError:
        with open("data.json", "w") as f:
            f.write("{\"Date\":[],\"BSL\":[]}")

    with open("data.json",) as file:
        healthdata = json.load(file)
        print(healthdata)

    healthdata["Date"].append(date_text.get())
    healthdata["BSL"].append(BSL_text.get())
    if len(healthdata["Date"])> 1:
        prediction = linear_reggression(a=healthdata["Date"], b=healthdata["BSL"])
        print(prediction)
        if 50 < prediction < 500:
            predictionlabel = Label(window, text=f"Prediction: {prediction}")
            predictionlabel.grid(row=1, column=2)

    with open("data.json", "w") as file:
        json.dump(healthdata, file)
    time.sleep(3)

def showgraph():
    with open("data.json",) as file:
        healthdata = json.load(file)
    plt.plot(healthdata["Date"], healthdata["BSL"])
    plt.ylabel("Blood Sugar Level")
    plt.xlabel("Date")
    plt.savefig("HEALTHPICS.png")
    test = ImageTk.PhotoImage(Image.open("HEALTHPICS.png"))
    panel = Label(window, image=test)
    panel.photo = test
    panel.grid(row=3, column=0, columnspan=3 )

def detailedgraph():
    with open("data.json",) as file:
        healthdata = json.load(file)
    plt.plot(healthdata["Date"], healthdata["BSL"])
    plt.ylabel("Blood Sugar Level")
    plt.xlabel("Date")
    plt.show()
   
    
    
    

Date = Label(window, text="Date:")
Date.grid(row=0, column=0)

date_text = StringVar()
DateEntry = Entry(window, textvariable=date_text)
DateEntry.grid(row=0, column=1)

BSL = Label(window, text="Blood Sugar Level:")
BSL.grid(row=1, column=0)

BSL_text = IntVar()
BSLEntry = Entry(window, text=BSL_text)
BSLEntry.grid(row=1, column=1)

update = Button(window, text="update", width=12, command=updatefun)
update.grid(row=2, column=1)

graph = Button(window, text="Show Graph", width=12, command=showgraph)
graph.grid(row=2, column=2)

graph2 = Button(window, text="Show Detailed Graph", width=18, command=detailedgraph)
graph2.grid(row=2, column=0)


window.mainloop()


