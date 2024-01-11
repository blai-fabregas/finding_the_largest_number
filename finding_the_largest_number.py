#Assignment #4 - Finding the Largest Number Among 3 Inputs
# Ask user to input 3 numbers
# Print and determine the largest among the 3 numbers


import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

base_path = Path(r"C:\\Users\\uella blainne\\Documents\\First Year\\Acads\\Programming Logics and Designs\\Assignment 4\\Images") 
output_path = Path (__file__).parent
assets_path = output_path / Path (r"C:\\Users\\uella blainne\\Documents\\First Year\\Acads\\Programming Logics and Designs\\Assignment 4\\Images")

def relative_to_assets(path: str) -> Path:
    return assets_path / Path(path)

class BackgroundFrame(tk.Frame):
    def __init__(self, parent, background_image_path):
        tk.Frame.__init__(self, parent)

        self.background_image = tk.PhotoImage (file = relative_to_assets(background_image_path))
        background_label = tk.Label (self, image=self.background_image)
        background_label.image = self.background_image
        background_label.place (
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )
class CanvasAndButton (tk.Frame):
    def __init__(self, parent,)
      tk.Frame.__init__(self, parent) 

      self.canvas = tk.Canvas(
          self,
          bg= "#FFFFFF"
          height=650,
          width=400
          bd=0
          highlightthickness=0,
          relief="ridge"
        ) 
      self.canvas.place (
          x=0,
          y=0
      )

      images = ["image_4.png", "image_5.png", "image_6.png"]
      for i, image_path in enumerate (images, start=1):
          image =  tk.PhotoImage (file = relative_to_assets (image_path))
          self.canvas.create_image(201.0,325.0 if i != 2 else 300.0, image=image)
      
      button_image_path = "button_2.png"
      button_image = tk.PhotoImage (file=relative_to_assets(image_path))
      self.button = tk.Button (
          self.canvas,
          image=button_image,
          borderwidth=0
          highlightthickness=0,
          command=lambda: print("button_2 clicked"),
          relief="flat"
      )
    self.button_2.place(
        x=68,
        y=515,
        width=279,
        height= 128
    )


# Making the Main Window
window = Tk()
window.title("Largest Number")
window.geometry ("400x620")
window.configure (bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 650,
    width = 400,
    relief = "ridge"
)

canvas.place (
    x = 0,
    y = 0)

