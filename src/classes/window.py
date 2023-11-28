import tkinter as tk
from typing import Optional

from PIL import ImageTk, Image

from src.classes.game import Game
from src.utils.parse import get_available_city_files, parse_cities, get_cities_as_coordinates
from src.utils.windows import calc_dist_window, add_city_window


class Window:
    def __init__(self):
        self.root = tk.Tk()

        # Initialize the StringVar for the dropdowns
        self.selected_city = tk.StringVar()
        self.selected_dimension = tk.StringVar()

        # Initialize other variables
        self.game: Optional[Game] = None
        self.highlighted: list[str] = []  # Store the names of the highlighted cities
        self.clicked_city: Optional[str] = None  # Store the name of the clicked city (to show the name)

        # Set the selected dimension option
        available_city_files = get_available_city_files()
        self.available_dimensions: list[str] = list(map(lambda c: c["label"], available_city_files))
        default_dimension = self.available_dimensions[0]
        self.selected_dimension.set(default_dimension)

        # Set the selected city option
        self.selected_city.set("Select a city")

        # Initialize canvas related variables
        self.canvas: Optional[tk.Canvas] = None
        self.image = ImageTk.PhotoImage(Image.open(f"src/assets/map_france_{default_dimension}.gif"))

    @property
    def parsed_cities(self):
        """
        Retourne les villes comme une liste de dictionnaires avec les propriétés lat et lng.
        """
        return parse_cities("src/assets/villes.txt")

    @property
    def cities_data(self):
        """
        Retourne les villes de la même manière que dans la propriété `parsed_cities` avec les propriétés x et y
        correspondant aux coordonnées de la ville dans la canvas.
        """
        return get_cities_as_coordinates(self.parsed_cities, self.width, self.height)

    @property
    def cities_name(self):
        """
        Retourne la liste avec le nom de toutes les villes.
        """
        return list(self.parsed_cities)

    @property
    def width(self):
        """
        Retourne la largeur de la dimension sélectionnée.
        """
        return int(self.selected_dimension.get().split('x')[0])

    @property
    def height(self):
        """
        Retourne la hauteur de la dimension sélectionnée.
        """
        return int(self.selected_dimension.get().split('x')[1])

    def draw_oval(self, x: int, y: int, radius: int, color: str, width: int):
        """
        Dessine un oval sur la canvas.

        :param x: La coordonnée x.
        :param y: La coordonnée y.
        :param radius: Le radius de l'ovale.
        :param color: La couleur du trait extérieure de l'ovale.
        :param width: La largeur du trait extérieure de l'ovale.
        """
        return self.canvas.create_oval(
            x - radius / 2,
            y - radius / 2,
            x + radius / 2,
            y + radius / 2,
            width=width,
            outline=color,
            fill="#FFFFFF"
        )

    def draw_canvas(self):
        """
        Dessine la canvas.
        """
        if self.canvas is not None:
            self.canvas.destroy()

        # Initialise la canvas
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        # Crée l'image sur la canvas
        self.image = ImageTk.PhotoImage(Image.open(f"src/assets/map_france_{self.selected_dimension.get()}.gif"))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Dessine les ovales sur la canvas
        for city, coords in self.cities_data.items():
            is_highlighted = city in self.highlighted

            color = "#0000FF" if is_highlighted else "#FF0000"
            radius = 15 if is_highlighted else 10

            oval = self.draw_oval(coords["x"], coords["y"], radius, color, 1)
            self.canvas.tag_bind(oval, "<Button-1>", self.on_click_city(city))

            # Affiche le nom de la ville si l'utilisateur a cliqué dessus
            if self.clicked_city == city:
                self.canvas.create_text(coords["x"], coords["y"] - 15, text=city, fill="#000000")

    def on_click_city(self, city: str):
        """
        Fonction d'exécution lorsqu'un utilisateur clique sur une ville.

        :param city: Le nom de la ville cliqué.
        """

        def core(_event):
            if self.game:
                self.game.play(city)

            self.clicked_city = city
            self.draw_canvas()

        return core

    def on_update_selected_dimension(self, _, __, ___):
        """
        Fonction d'exécution lorsqu'un utilisateur sélectionne une valeur dans le dropdown de sélection de dimension.
        """
        self.draw_canvas()

    def on_update_selected_city(self, _, __, ___):
        """
        Fonction d'exécution lorsqu'un utilisateur sélectionne une ville dans le dropdown de sélection de ville.
        """
        self.highlighted = [self.selected_city.get()]
        self.draw_canvas()

    def add_listeners(self):
        """
        Ajoute les fonctions d'écoute sur les StringVar des dropdowns.
        """
        self.selected_city.trace("w", self.on_update_selected_city)
        self.selected_dimension.trace("w", self.on_update_selected_dimension)

    def start_game(self):
        """
        Fonction d'exécution du lançement du jeu.
        """

        def core():
            def stop():
                self.game = None

            self.game = Game(self.cities_name, stop)
            self.game.start()

        return core

    def setup(self):
        """
        Fonction de mise en place de la fenêtre.
        :return:
        """
        # Crée le bouton d'ajout d'une nouvelle ville
        add_city_button = tk.Button(self.root, text="Ajouter une nouvelle ville", command=add_city_window)
        add_city_button.pack()

        # Crée le dropdown de sélection d'une dimension
        dimensions_dropdown = tk.OptionMenu(self.root, self.selected_dimension, *self.available_dimensions)
        dimensions_dropdown.pack()

        # Crée le dropdown de sélection d'une ville
        cities_dropdown = tk.OptionMenu(self.root, self.selected_city, *self.cities_name)
        cities_dropdown.pack()

        # Créer le bouton de lançement du jeu
        start_game_button = tk.Button(self.root, text='Jouer', command=self.start_game())
        start_game_button.pack()

        # Créer le bouton d'affichage de la fenêtre de calcul de distance
        calc_dist_button = tk.Button(self.root, text="Calculer une distance",
                                     command=lambda: calc_dist_window(self.parsed_cities))
        calc_dist_button.pack()

    def start(self):
        """
        Exécute la fenêtre.
        """
        self.setup()
        self.add_listeners()
        self.draw_canvas()
        self.root.mainloop()
