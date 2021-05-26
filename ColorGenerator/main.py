import random
from tkinter import *
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

from scipy.spatial import KDTree


# creating the color variables
colorR = 0
colorG = 0
colorB = 0
color = []

def open_window(window_color):
    window = Tk()

    window.title("Color Generator")

    window.configure(width=500, height=300)

    window.configure(bg=f'{window_color}')

    window.mainloop()


def convert_rgb_to_names(rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'{names[index]}'

def generate_and_window():

    #setting the values to the variables
    colorR = random.choice(range(256))
    colorG = random.choice(range(256))
    colorB = random.choice(range(256))
    color = [colorR, colorG, colorB]
    color_window = (convert_rgb_to_names((color)))
    print(color)
    print(color_window)
    open_window(color_window)

generate_and_window()