import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


read_data = pd.read_excel("covid_19_data.xlsx")
'''
x_values = ["Total Deaths", "Total Recovered"]
x = np.arange(len(x_values))
list(x)
plt.xticks(x, x_values)

y = [read_data["Total Deaths"], read_data["Total Recovered"]]

plt.bar(x, y)
'''
y = read_data["Total Deaths"], read_data["Total Recovered"]


print(y)

#plt.bar([0, 1], y)
#plt.show()
