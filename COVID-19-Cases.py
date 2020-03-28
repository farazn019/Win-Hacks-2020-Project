from bs4 import BeautifulSoup
import requests



url = "https://www.worldometers.info/coronavirus/"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, "html.parser")

global_case_information = soup.find_all("div", {"class":"maincounter-number"})

'''Since there are no unary operators supported between 'counter' and the variable 'i',
I must declare another variable 'counter' and set it equal to zero, with the value
of counter being updated by 1 each time.'''


total_cases = []
counter = 0;
for cases in global_case_information:
    if(counter == 13):
        break
    else:
        total_cases.append(cases.text)
        print(cases.text)
        counter += 1    

num = 0;
for case in total_cases:
    print(num, '->', case)
    num += 1

