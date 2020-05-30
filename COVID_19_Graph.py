#All the necessary libraries are imported.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd


#This function will create a graph of COVID_19 cases, deaths, and numbers infected throughout the world
def COVID_graph():
    #Here we deal with the x-axis of the bar graph.
    x_values = ["Total Deaths", "Total Recovered", "Total Infected"]
    x = np.arange(len(x_values))
    list(x)
    plt.xticks(x, x_values)



    #Here we deal with the y-axis of the graph.

    book = xlrd.open_workbook("covid_19_data.xlsx")
    sheet = book.sheet_by_index(0)


    y = [] #This list will store all the integer values for: Total Deaths, Total Recovered, and Total Infected.

    column_cell = 1
    while (column_cell <= 3):
        current_cell = str(sheet.cell(1, column_cell))
        current_value=""
        for number in current_cell:
            if number in "0123456789": 
                current_value += number
        current_value = int (current_value) #The string is typecasted to an integer, so it can be stored in the list (the list holds values for the y-axis).
        y.append(current_value)
        column_cell += 1

    #Informs the user that the integer values are in millions.
    plt.ylabel("Deaths In Millions") 
    plt.title("COVID-19 Cases WorldWide")

    plt.bar(x, y) #Plots the bar graph
    for index, value in enumerate(y):
        plt.text(x[index] - 0.25, value + 0.1, str(value)) #Shows the value of each bar graph on top of the bars.


    plt.show() #Shows the bar graph
