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
highlighted = []  # { "x": int, "y": int }


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

    def draw_oval(x: int, y: int, radius: int, color: str, width: int):
        canvas.create_oval(x - radius / 2, y - radius / 2, x + radius / 2, y + radius / 2, width=width, outline=color)

    for city, coords in cities_data.items():
        draw_oval(coords["x"], coords["y"], 10, "#FF0000", 1)

    for coords in highlighted:
        draw_oval(coords["x"], coords["y"], 15, "#0000FF", 3)


def on_selected_city_update(_, __, ___):
    draw_canvas()


selected_city.trace('w', on_selected_city_update)

draw_canvas()

root.mainloop()
