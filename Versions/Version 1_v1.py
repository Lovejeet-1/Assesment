"""""""""""""""""""""
Version 1 of program 
"""""""""""""""""""""

import tkinter as tk

"""""""""""""""
Component 1 - V2
"""""""""""""""
welcomebuttons_colour = bg = "#2cdfdd"

welcomebackground_colour = "#f3f1eb"

class WelcomePage:
    def __init__(self):

        #Window
        self.root = tk.Tk()
        self.root.title("Welcome Page")
        self.root.resizable(False, False)
        self.root.geometry("1200x800")
        self.root.configure(welcomebackground_colour)

        #Load and Resize image
        self.logo = tk.PhotoImage(file = "Logofinal.png") 
        self.logo = self.logo.subsample(4) 
        
        #Create Widgets
        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):

        #logo
        logo_label = tk.Label(self.root, image=self.logo, bg= welcomebackground_colour)
        logo_label.pack(side="top", ipady=40, padx=10, pady=40, expand=True, fill="both" )

        #continue button
        button_continue = tk.Button(self.root, text = "Continue".title(), bg = welcomebuttons_colour, fg = "White", font = ("Times New Roman", 35, "bold"), width = 20, command = self.to_map)
        button_continue.pack(side="right" , ipady=10, padx = 10, pady = 10)

        #quit button
        button_quit = tk.Button(self.root, text = "Quit", bg = welcomebuttons_colour, fg = "white",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.quit_app)
        button_quit.pack(side="top", ipady=10, padx = 10, pady = 10)

    def quit_app(self):
        self.root.destroy()

    def to_map(self):
        self.root.destroy()
        MapScreen




"""""""""""""""
Component 2 - V1
"""""""""""""""

class MapScreen:
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
        
        #setup map
        map_label = tk.Label(self.root, image=self.map, bg = "black", borderwidth = 0, )
        map_label.pack(expand = True, fill="both")

        #Buttons for all the different cruise ship lines offered
        button_Europe = tk.Button(self.root, fg = "White", image = self.red_button,)
        button_Europe.pack(side="bottom" )
        
        button_Asia = tk.Button(self.root, fg = "White", image = self.red_button,)
        button_Asia.pack(side="bottom" )

        button_Pacific = tk.Button(self.root, fg = "White", image = self.red_button,)
        button_Pacific.pack(side="bottom" )

        button_SouthAmerica = tk.Button(self.root, fg = "White", image = self.red_button,)
        button_SouthAmerica.pack(side="bottom" )

        button_NorthAmerica = tk.Button(self.root, fg = "White", image = self.red_button,)
        button_NorthAmerica.pack(side="bottom" )

        button_AfricaMiddleEast = tk.Button(self.root, fg = "White", image = self.red_button,)
        button_AfricaMiddleEast.pack(side="bottom" )

        #Button to go back to welcome page
        button_Back = tk.Button(self.root, fg = "White", image = self.red_button,)
        button_Back.pack(side="bottom" )


    def back_to_welcome(self):
        self.root.destroy
        WelcomePage()
    


"""""""""""
Run Program
"""""""""""

if __name__== "__main__":
    WelcomePage()
    