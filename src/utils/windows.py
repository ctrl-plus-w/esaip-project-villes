import tkinter as tk

from geopy.distance import geodesic

from src.utils.add_city import add_city as add_city_back


def add_city_window():
    """
    Créer la fenêtre de création d'une ville.
    """
    root = tk.Toplevel()
    root.wm_title("Window")

    # Champ d'entrée du nom de la ville
    city_label = tk.Label(root, text="Nom de la ville")
    city_label.grid(row=0, column=0)
    city_entry = tk.Entry(root)
    city_entry.grid(row=0, column=1)

    # Champ d'entrée de la latitude
    latitude_label1 = tk.Label(root, text="Latitude")
    latitude_label1.grid(row=1, column=0)
    latitude_entry = tk.Entry(root)
    latitude_entry.grid(row=1, column=1)
    latitude_label2 = tk.Label(root, text="°")
    latitude_label2.grid(row=1, column=2)
    latitude_entry2 = tk.Entry(root)
    latitude_entry2.grid(row=1, column=3)
    latitude_label3 = tk.Label(root, text="'N")
    latitude_label3.grid(row=1, column=4)

    # Champ d'entrée de la longitude
    longitude_label = tk.Label(root, text="Longitude")
    longitude_label.grid(row=2, column=0)
    longitude_entry = tk.Entry(root)
    longitude_entry.grid(row=2, column=1)
    longitude_label2 = tk.Label(root, text="°")
    longitude_label2.grid(row=2, column=2)
    longitude_entry2 = tk.Entry(root)
    longitude_entry2.grid(row=2, column=3)

    # Options du dropdown de sélection de la direction
    options = ["W", "E"]

    selected_direction = tk.StringVar()
    selected_direction.set(options[0])

    # Champ d'entrée de la direction des coordonées
    drop = tk.OptionMenu(root, selected_direction, *options)
    drop.grid(row=2, column=4)

    def on_save():
        """
        Fonction de sauvegarde des données entrée dans le formulaire.
        """
        lat = f"{latitude_entry.get()}° {latitude_entry2.get()}'N"
        lng = f"{longitude_entry.get()}° {longitude_entry2.get()}'{selected_direction}"

        add_city_back(city_entry.get(), lat, lng)

    # Bouton de sauvegarde
    save = tk.Button(root, text="Sauvegarder", command=on_save)
    save.grid(row=4, column=0)

    # Exit button
    b = tk.Button(root, text="Quitter", command=root.destroy)
    b.grid(row=4, column=1)


def calc_dist_window(cities):
    """
    Créer la fenêtre de calcul de distance entre deux villes.

    :param cities: La liste des villes disponibles (dictionnaires avec lat et lng en propriétés)
    """
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
        """
        Fonction d'écoute de l'événement de mise à jour d'un dropdown.
        """
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
