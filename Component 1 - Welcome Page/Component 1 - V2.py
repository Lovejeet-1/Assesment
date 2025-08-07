"""""""""""""""
Component 1 - V2
"""""""""""""""
import tkinter as tk

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

    def run(self):
         self.root.mainloop()


program = WelcomePage()
program.run() 