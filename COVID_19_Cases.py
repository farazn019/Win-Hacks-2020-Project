from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd 

def global_data():
    
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    
        
    '''Since there are no unary operators supported between 'counter' and the variable 'i',
    I must declare another variable 'counter' and set it equal to zero, with the value
    of counter being updated by 1 each time.'''
    total_cases = []
    counter = 0;
    global_case_information = soup.find_all("div", {"class":"maincounter-number"})
    for cases in global_case_information:
        if(counter == 13):
            break
        else:
            total_cases.append(cases.text)
            counter += 1

    data = pd.DataFrame({"Total Deaths":[total_cases[1]] , "Total Recovered":[total_cases[2]], "Total Infected":[total_cases[0]]})

    writer = pd.ExcelWriter("covid_19_data.xlsx", engine="xlsxwriter")
    data.to_excel(writer)

    writer.save()
    
global_data()
    
