import tkinter as tk

from PIL import Image, ImageTk

from src.back.parse import parse_cities, get_cities_as_coordinates

root = tk.Tk()

canvas = tk.Canvas(root, width=494, height=516)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("src/assets/map_france_494x516.gif"))
canvas.create_image(0, 0, anchor=tk.NW, image=img)

cities = get_cities_as_coordinates(parse_cities('src/assets/villes.txt'))

for city, coords in cities.items():
    radius = 10
    x = coords["x"]
    y = coords["y"]

    canvas.create_oval(x - radius / 2, y - radius / 2, x + radius / 2, y + radius / 2, outline="#ff0000")

root.mainloop()
