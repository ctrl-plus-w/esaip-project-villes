import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from src.back.add_city import add_city as add_city_back
from src.back.find_city import find_city
from src.back.game import Game
from src.back.parse import get_available_cities, get_cities_as_coordinates, parse_cities

root = tk.Tk()
cities = get_available_cities()

# Get cities name
cities_name = list(parse_cities("src/assets/villes.txt"))
selected_city_atlas = tk.StringVar()
selected_city_atlas.set(cities_name[0])

# Create dropdown menu for atlas
drop_atlas = tk.OptionMenu(root, selected_city_atlas, *cities_name)
drop_atlas.pack()

# Dropdown menu options
options = list(map(lambda c: c["label"], cities))

selected_dimension = tk.StringVar()
selected_dimension.set(options[0])

# Create Dropdown menu
drop = tk.OptionMenu(root, selected_dimension, *options)
drop.pack()

img = ImageTk.PhotoImage(Image.open(f"src/assets/map_france_{selected_dimension.get()}.gif"))

canvas = None
width, height = None, None
highlighted = []  # { "x": int, "y": int }


def draw_canvas():
    global canvas
    global width
    global height

    width = int(selected_dimension.get().split('x')[0])
    height = int(selected_dimension.get().split('x')[1])

    if canvas:
        canvas.destroy()

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    global img
    img = ImageTk.PhotoImage(Image.open(f"src/assets/map_france_{selected_dimension.get()}.gif"))

    canvas.create_image(0, 0, anchor=tk.NW, image=img)

    cities_data = get_cities_as_coordinates(parse_cities('src/assets/villes.txt'), width, height)

    def draw_oval(x: int, y: int, radius: int, color: str, width: int):
        canvas.create_oval(x - radius / 2, y - radius / 2, x + radius / 2, y + radius / 2, width=width, outline=color)

    for city, coords in cities_data.items():
        draw_oval(coords["x"], coords["y"], 10, "#FF0000", 1)

    for coords in highlighted:
        draw_oval(coords["x"], coords["y"], 15, "#0000FF", 3)


def on_selected_dimension_update(_, __, ___):
    draw_canvas()


def on_selected_city_atlas_update(_, __, ___):
    global highlighted
    global width
    global height

    #  Get the city lng and lat
    cities = {
        selected_city_atlas.get(): find_city(selected_city_atlas.get()),
        "NorthWest": ({"lat": 52, "lng": -5.5}),
        "SouthEst": ({"lat": 41, "lng": 10.5})
    }

    cities_data = get_cities_as_coordinates(cities, width, height)
    print(cities_data)

    # Convert gps coordinates to x,y points on the map 
    highlighted = [{
        "x": cities_data[selected_city_atlas.get()]['x'],
        "y": cities_data[selected_city_atlas.get()]['y']
    }]

    # Draw points of the map again
    draw_canvas()


def play_game():
    win = tk.Toplevel()
    win.wm_title("Window")

    game = Game()

    print(game.coups_restants)
    while game.coups_restants > 0:
        # Play a round
        city, coups, score = game.play_round()

        # Show round information  
        label = tk.Label(win, text=f"Situez {city} sur la carte\nCoups restants: {coups}\nScore: {score}")
        label.pack()

        #  Abandonner button
        surrender = ttk.Button(win, text="Abandonner", command=win.destroy)
        surrender.pack()

        # Wait for the user to click a city
        # sleep(10)

    #  Show game stats, re-create the window
    win.destroy()
    win = tk.Toplevel()
    win.wm_title("Window")

    _, coups, score = game.get()
    label = tk.Label(win,
                     text=f"Vous avez trouvé {score} villes sur 20\nCela correspond à {score / 20 * 100} % de réussite")

    #  Buttons
    # play_again = ttk.Button(win, text='Rejouer', command=play_game)
    # play_again.grid(row=0, column=1)
    quit = ttk.Button(win, text="Quitter le jeu", command=win.destroy)
    quit.grid(row=0, column=0)


def add_city():
    win = tk.Toplevel()
    win.wm_title("Window")

    # Name of the city
    city_label = tk.Label(win, text="City name")
    city_label.grid(row=0, column=0)
    city_entry = tk.Entry(win)
    city_entry.grid(row=0, column=1)

    # Latitude    
    latitude_label1 = tk.Label(win, text="Latitude")
    latitude_label1.grid(row=1, column=0)
    latitude_entry = tk.Entry(win)
    latitude_entry.grid(row=1, column=1)
    latitude_label2 = tk.Label(win, text="°")
    latitude_label2.grid(row=1, column=2)
    latitude_entry2 = tk.Entry(win)
    latitude_entry2.grid(row=1, column=3)
    latitude_label3 = tk.Label(win, text="'N")
    latitude_label3.grid(row=1, column=4)

    #  Longitude
    longitude_label = tk.Label(win, text="Longitude")
    longitude_label.grid(row=2, column=0)
    longitude_entry = tk.Entry(win)
    longitude_entry.grid(row=2, column=1)
    longitude_label2 = tk.Label(win, text="°")
    longitude_label2.grid(row=2, column=2)
    longitude_entry2 = tk.Entry(win)
    longitude_entry2.grid(row=2, column=3)

    # Dropdown menu options
    options = ["W", "E"]

    selected_direction = tk.StringVar()
    selected_direction.set(options[0])

    # Create Dropdown menu
    drop = tk.OptionMenu(win, selected_direction, *options)
    drop.grid(row=2, column=4)

    # Save
    save = ttk.Button(win, text="Save", command=lambda: add_city_back(
        city_entry.get(),
        f"{latitude_entry.get()}° {latitude_entry2.get()}'N",
        f"{longitude_entry.get()}° {longitude_entry2.get()}'{selected_direction}"
    ))
    save.grid(row=4, column=0)

    # Exit button
    b = ttk.Button(win, text="Exit", command=win.destroy)
    b.grid(row=4, column=1)


# New city button
button_add_map = tk.Button(root, text="Add a new city", command=add_city)
button_add_map.pack()

# Jouer button
button_game = tk.Button(root, text='Jouer', command=play_game)
button_game.pack()

selected_dimension.trace('w', on_selected_dimension_update)
selected_city_atlas.trace('w', on_selected_city_atlas_update)

draw_canvas()

root.mainloop()
