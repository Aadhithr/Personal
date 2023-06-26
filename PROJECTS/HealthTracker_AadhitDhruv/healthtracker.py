from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import time
import json
import math


#added
with open("data.json", "a") as file:
    pass

with open("data.json", "w") as file:
    file.write("[{'Date':[],'BSL':[]}")
#added


window = Tk()
window.title("Health Tracker")
window.geometry("400x200")

#added
def linear_reggression(a=[], b=[]):
    dates = []
    for x in a:
        date = x.split("-")
        date = (int(date[0])-1)*31 + int(date[1])
        dates.append(date)
        print(dates)
    print(dates)
    nor_dates = []
    for date in dates:
        date = date - (dates[0] -1)
        nor_dates.append(date)
    dates = nor_dates
    print(dates)
    nor_b = []
    for B in b:
        nor_b.append(B/10)
    b = nor_b
    print(b)
    avg_dates = math.fsum(dates)/len(dates)
    avg_BSL = math.fsum(b)/len(b)
    dates_MAD = []
    BSL_MAD = []
    print(avg_BSL, " ", avg_dates)
    for date in dates:
        dates_MAD.append(date-avg_dates)
    for B in b:
        BSL_MAD.append(B-avg_BSL)
    slope_y = []
    print(dates_MAD, " ", BSL_MAD)
    for x in range(len(b)):
        slope_y.append(BSL_MAD[x] * BSL_MAD[x])
    dates_MAD_2 = [int(x)^2 for x in dates_MAD]
    slope = math.fsum(slope_y)/math.fsum(dates_MAD_2)
    print("slope =", slope)
    y_int = avg_BSL/(avg_dates*slope)
    print("y int", y_int)
    n_date = dates[-1]+1
    print(n_date)
    equation_line = slope*n_date + y_int
    print(equation_line)
    return(equation_line*10)
#added

def updatefun():                     #fixed file
    with open("data.json") as file:
        healthdata = json.load(file)
    healthdata[0]["Date"].append(date_text.get())
    healthdata[0]["BSL"].append(BSL_text.get())
    #added
    if healthdata[0]["Date"].length > 1:
        prediction = linear_reggression(a=healthdata[0]["Date"], b=healthdata[0]["BSL"])

    with open("data.json", "w") as file:
        json.dump(healthdata, file)
    time.sleep(3)
    plt.plot(healthdata[0]["Date"], healthdata[0]["BSL"])
    plt.ylabel("Blood Sugar Level")
    plt.xlabel("Date")
    plt.savefig("pics.png")
    test = ImageTk.PhotoImage(Image.open("C:\Work\Code\PythonCourse\homework\my_extraworks\HealthTracker_AadhitDhruv\matplotlibpics\pics.png"))
    panel = Label(window, image=test)
    panel.photo = test
    panel.grid(row=3, column=2, columnspan=3 )


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

window.mainloop()
