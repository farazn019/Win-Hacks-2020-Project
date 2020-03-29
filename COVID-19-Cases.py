from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt


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
            print(cases.text)
            counter += 1    


    global_cases = {"Total Deaths":total_cases[1], "Total Recovered":total_cases[2], "Total Cases":total_cases[0]}

    for key, value in global_cases.items():
        print(key, '->', value)

    
    covid_figure = plt.figure()

    plt.rcParams["figure.figsize"] = [40, 40]
    keys_array = np.arange(len(global_cases.keys()))
    plt.xticks(keys_array, global_cases.keys())
    plt.ylabel("Number Of People Affected(Globally)")
    plt.title("Global Covid-19 Statistics")

    plt.yticks([0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000])
    plt.bar(keys_array, global_cases.values())
    plt.show()
    

    
global_data()
