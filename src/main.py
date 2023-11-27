import tkinter as tk

from PIL import Image, ImageTk

from src.back.parse import get_available_cities, get_cities_as_coordinates, parse_cities

root = tk.Tk()
cities = get_available_cities()

# Dropdown menu options
options = list(map(lambda c: c["label"], cities))

selected_city = tk.StringVar()
selected_city.set(options[0])

# Create Dropdown menu
drop = tk.OptionMenu(root, selected_city, *options)
drop.pack()

img = ImageTk.PhotoImage(Image.open(f"src/assets/map_france_{selected_city.get()}.gif"))

canvas = None


def draw_canvas():
    global canvas

    width = int(selected_city.get().split('x')[0])
    height = int(selected_city.get().split('x')[1])

    if canvas:
        canvas.destroy()

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    global img
    img = ImageTk.PhotoImage(Image.open(f"src/assets/map_france_{selected_city.get()}.gif"))

    canvas.create_image(0, 0, anchor=tk.NW, image=img)

    cities_data = get_cities_as_coordinates(parse_cities('src/assets/villes.txt'), width, height)

    for city, coords in cities_data.items():
        radius = 10
        x = coords["x"]
        y = coords["y"]

        canvas.create_oval(x - radius / 2, y - radius / 2, x + radius / 2, y + radius / 2, outline="#ff0000")


button = tk.Button(root, text="Update the city", command=lambda: draw_canvas())
button.pack()

draw_canvas()

root.mainloop()
