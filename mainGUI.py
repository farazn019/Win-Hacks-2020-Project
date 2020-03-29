#Created By Faraz Naseem.

#All the necessary core libraries are imported.
import tkinter as tk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

#Another page is imported.
from facts_page import facts

#This is the class to create the facts window.
class FactsWindow:
    def __init__(self, master, text, side):
        self.master = master
        self.master.geometry("700x700")
        self.frame = tk.Frame(self.master)
        self.text = text
        self.button = tk.Button(self.master, text = self.text, width = 20, command = self.new_window)
        self.side = side
        self.button.pack(side=self.side)
        
        self.frame.pack()

    def new_window(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.geometry("900x900")
        self.new_window.configure(bg="#3399ff")
        self.new_window.title("Important Facts About Covid-19")
        facts(self.new_window)


#This function graphs to curves, with the aim of showing the impact of flattening the curve.
def graphCanvas(main_page): 
    f = Figure(figsize = (1, 1), dpi = 100)

    #This is all the information for plotting the curve without any precautions or measures taken.
    a = f.add_subplot(111)
    top_curve = a
    x1 = np.arange(0, np.pi, 0.01)
    y1 = np.sin(x1)
    top_curve.plot(x1, y1, label="Without Protective Measures")

    #This is all the information for plotting the curve when precautions and government measures are taken.
    bottom_curve = a
    x2 = np.arange(0, np.pi, 0.01)
    y2 = np.abs(0.5 * (np.sin(x2)))
    bottom_curve.plot(x2, y2, label="With Protective Measures")

    #A horizontal line is created.
    horizontal_line = a
    x3 = [0, np.pi]
    y3 = [0.501, 0.501]
    horizontal_line.plot(x3, y3, linestyle= '--', label="Hospital Carrying Capacity")

    #Some important properties and visuals for the graph itself are defined.
    a.set_xlabel("Total Number Of People Infected")
    a.set_ylabel("Time Since First Infection")
    a.set_xlim(0, np.pi)
    a.set_ylim(0, 1.5)
    a.set_yticklabels([])
    a.set_xticklabels([])

    #A legend is created
    f.legend()    
    
    canvas = FigureCanvasTkAgg(f, master = main_page)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    #A toolbar is created.
    toolbar = NavigationToolbar2Tk(canvas, main_page)
    toolbar.update()
    canvas.get_tk_widget().pack(side='top', fill='both')



#This is the main function.
def main():

    #This is the root (home page), and all the modifications made to the root.
    root = tk.Tk()
    root.title("COVID 19: HOME")

    theme = tk.Label(root, text="#Flatten The Curve", fg="#FF3333", bg="#FFFF33")
    theme.config(font="Verdana 32 bold")
    theme.pack(side='top')

    root.configure(background='#FFFF33')
    
    graphCanvas(root)
    #graph_window = Window(root, "Graph Visualization", "left")
    facts_window = FactsWindow(root, "Important Facts", "right")
    #prevention_window = Window(root, "Prevention Techniques", "bottom")


    root.mainloop()


#The main function is called.
main()
