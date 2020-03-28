import tkinter as tk


class Window:
    def __init__(self, master, x, y):
        self.master = master
        self.master.geometry("700x700")
        self.frame = tk.Frame(self.master)
        self.button = tk.Button(self.master, text = "Graph Visualization", width = 20, command = self.new_window)
        self.button.pack(side="bottom")
        self.frame.pack()

    
    def new_window(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.geometry("700x700")



def main():

    #This is the root (home page), and all the modifications made to the root.
    root = tk.Tk()
    root.title("COVID 19: HOME")
    root.configure(background='#FFFF33')

    
    page_one = Window(root, 2, 2)
    root.mainloop()

    page_two = Window(root)


main()
