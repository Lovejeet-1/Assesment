import tkinter as tk

"""""""""""""""
Component 2 - V1
"""""""""""""""

class WelcomePage:
    def __init__(self):

        #Window
        self.root = tk.Tk()
        self.root.title("Welcome Page")
        self.root.resizable(False, False)
        self.root.geometry("1200x800")
        self.root.configure("white")

        self.create_widgets()

        self.root.mainloop()

        #load images
        self.map = tk.PhotoImage(file = "Global_Map.png")

        self.red_button = tk.PhotoImage(file = "red_button.png")
        self.red_button = self.red_button.subsample(4)

        #widgets
    def create_widgets(self):
        button_europe = tk.Button(self.root, fg = "White", image = self.red_button, )
        button_europe.pack(side="bottom" )

        map_label = tk.Label(self.root, image=self.map, bg = "black", borderwidth = 0, )
        map_label.pack(expand = True, fill="both")

        self.root.mainloop()


