import tkinter as tk
from tkinter import ttk

class PlayerMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create a title label
        self.title_label = ttk.Label(self, text="Settlers of Catan")
        self.title_label.grid(column=0, row=0, columnspan=2)

        # Create a label and entry for player name
        self.name_label = ttk.Label(self, text="Enter your name:")
        self.name_label.grid(column=0, row=1, sticky=tk.W)
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(column=1, row=1)

        # Create a label and combo box for player color
        self.color_label = ttk.Label(self, text="Choose your color:")
        self.color_label.grid(column=0, row=2, sticky=tk.W)

        # Create a color dictionary for Settlers of Catan
        catan_colors = {
            "Red": "#ff0000",
            "Blue": "#0000ff",
            "Orange": "#ffa500",
            "White": "#ffffff"
        }

        # Create a radio button for each color
        self.color_var = tk.StringVar()
        self.color_var.set("Red")
        for i, color in enumerate(catan_colors.keys()):
            rb = ttk.Radiobutton(self, text=color, variable=self.color_var, value=color,
                                 command=lambda c=color: self.update_color(catan_colors[c]))
            rb.grid(column=i, row=3)

        # Create a button to start the game
        self.start_button = ttk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.grid(column=1, row=4)

        # Set the default player color to red
        self.update_color(catan_colors["Red"])

    def update_color(self, color):
        # Update the color label to display the selected color
        self.color_label.configure(foreground=color)
        self.color_label.configure(text=f"Choose your color ({color}):")

    def start_game(self):
        # Retrieve the player name and color
        name = self.name_entry.get()
        color = self.color_var.get()

        # Start the game with the selected player name and color
        print(f"Starting game with player name: {name}, and color: {color}")


root = tk.Tk()
app = PlayerMenu(master=root)
app.mainloop()
