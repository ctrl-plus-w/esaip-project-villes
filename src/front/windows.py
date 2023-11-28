import tkinter as tk

from geopy.distance import geodesic

from src.back.add_city import add_city as add_city_back


def add_city_window():
    win = tk.Toplevel()
    win.wm_title("Window")

    # Name of the city
    city_label = tk.Label(win, text="Nom de la ville")
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
    save = tk.Button(win, text="Sauvegarder", command=lambda: add_city_back(
        city_entry.get(),
        f"{latitude_entry.get()}° {latitude_entry2.get()}'N",
        f"{longitude_entry.get()}° {longitude_entry2.get()}'{selected_direction}"
    ))
    save.grid(row=4, column=0)

    # Exit button
    b = tk.Button(win, text="Quitter", command=win.destroy)
    b.grid(row=4, column=1)


def calc_dist_window(cities):
    cities_name = list(cities)

    root = tk.Toplevel()
    root.wm_title('Calcul de la distance')

    city1_var = tk.StringVar()
    city1_dropdown = tk.OptionMenu(root, city1_var, *cities_name)
    city1_dropdown.pack()

    city2_var = tk.StringVar()
    city2_dropdown = tk.OptionMenu(root, city2_var, *cities_name)
    city2_dropdown.pack()

    label = tk.Label(root, text="")
    label.pack()

    def on_city_update(_, __, ___):
        city1 = city1_var.get()
        city2 = city2_var.get()

        if city1 and city2:
            coords1 = (cities[city1]["lat"], cities[city1]["lng"])
            coords2 = (cities[city2]["lat"], cities[city2]["lng"])

            dist = geodesic(coords1, coords2).kilometers
            label.config(text=f"Distance : {int(dist)}kms")

    city1_var.trace('w', on_city_update)
    city2_var.trace('w', on_city_update)

    exit_button = tk.Button(root, text="Quitter", command=root.destroy)
    exit_button.pack()
