
#All the necessary libraries are imported.
import tkinter as tk
from PIL import Image, ImageTk

'''This is the function where the image will be posed to the page, and
this function contains various facts about Covid-19.'''
def facts(page):

    #An image is opened and loaded.
    load = Image.open("coronavirus-factsheet-eng.jpg")
    render = ImageTk.PhotoImage(load)

    img = tk.Label(image = render)
    img.image = render

    img_label = tk.Label(page, image=render)
    img_label.place(x = 0, y = 0)

    #A list of seven facts about Covid-19. They all have a font of 12, and are coloured red.
    fact_one = tk.Label(page, text="Symptoms are:\n-Fever\n-Coughing\n-Sneezing", font="Arial 12 bold", fg="red").place(x = 0, y = 600)
    fact_two = tk.Label(page, text="Currently, there are no vaccines or cures\nfor COVID-19, as it is a new strain\nof the model coronavirus.", font="Arial 12 bold", fg="red").place(x = 500, y = 0)
    fact_three = tk.Label(page, text="This virus affect the elderly the most,\nas people above the age of 65 have the\nhighest death rate from Covid-19.", font="Arial 12 bold", fg="red").place(x = 500, y = 100)
    fact_four = tk.Label(page, text="There are many things that individuals can do,\nto prevent the spread of Covid-19, which includes:\n-Washing Hands Regularly\n-Avoiding Close Contact With Other Indidividuals\n-Covering Your Mouth And Nose When You Sneeze\n-Staying Home To Self-Isolate", font="Arial 12 bold", fg="red").place(x = 500, y = 275)
    fact_five = tk.Label(page, text="The COVID-19 strain of the coronavirus,\noriginated in Wuhan, China on November 17, 2019.", font="Arial 12 bold", fg="red").place(x = 500, y = 425)
    fact_six = tk.Label(page, text="Currently, the United States Of America\nhas the most infections in the world, with more than\n 100000 people having been infected by the virus.", font="Arial 12 bold", fg="red").place(x = 500, y = 525)
    fact_seven = tk.Label(page, text="Globally, this virus has infected\nmore than 650000 people, and claimed\nthe lives of more than 30000 people.", font="Arial 12 bold", fg="red").place(x= 140, y = 550)



