import random
import tkinter as tk
from typing import Optional

from PIL import Image, ImageTk

from src.back.parse import get_available_city_files, parse_cities, get_cities_as_coordinates
from src.front.windows import add_city_window, calc_dist_window


class Game:
    def __init__(self, available_cities: list[str], stop):
        self.stop = stop
        self.default_available_cities = available_cities
        self.available_cities = available_cities

        self.total_plays = 20
        self.remaining_plays = self.total_plays
        self.score = 0

        self.seeked_city = random.choice(self.available_cities)

        self.root = tk.Toplevel()

    def reset(self):
        self.available_cities = self.default_available_cities
        self.remaining_plays = self.total_plays
        self.score = 0

        self.seeked_city = random.choice(self.available_cities)
        self.draw_game()

    def draw_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.remaining_plays == 0:
            percentage = int(self.score / self.total_plays * 100)

            text = [
                f"Vous avez trouvé {self.score} villes",
                f"Cela correspond à {percentage}% de réussite",
            ]

            label = tk.Label(self.root, text="\n".join(text))
            label.pack()

            skip_button = tk.Button(self.root, text="Quitter", command=lambda: self.quit())
            skip_button.pack()

            reset_button = tk.Button(self.root, text="Rejouer", command=lambda: self.reset())
            reset_button.pack()
        else:
            text = [
                f"Situez {self.seeked_city} sur la carte",
                f"Coups restants: {self.remaining_plays}",
                f"Score: {self.score}",
            ]

            label = tk.Label(self.root, text="\n".join(text))
            label.pack()

            skip_button = tk.Button(self.root, text="Abandonner", command=lambda: self.play(""))
            skip_button.pack()

    def play(self, city: str):
        if city == self.seeked_city:
            self.score += 1

        # Decrement the total of remaining plays
        self.remaining_plays -= 1

        # Removed the city from the available cities and update the seeked city randomly
        self.available_cities.remove(self.seeked_city)
        self.seeked_city = random.choice(self.available_cities)

        self.draw_game()

    def start(self):
        self.draw_game()

    def quit(self):
        self.root.destroy()
        self.stop()


class CitiesWindow:
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
        return parse_cities("src/assets/villes.txt")

    @property
    def cities_data(self):
        return get_cities_as_coordinates(self.parsed_cities, self.width, self.height)

    @property
    def cities_name(self):
        return list(self.parsed_cities)

    @property
    def width(self):
        return int(self.selected_dimension.get().split('x')[0])

    @property
    def height(self):
        return int(self.selected_dimension.get().split('x')[1])

    def draw_oval(self, x: int, y: int, radius: int, color: str, width: int):
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
        if self.canvas is not None:
            self.canvas.destroy()

        # Initialize the canvas
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        # Create the canvas image
        self.image = ImageTk.PhotoImage(Image.open(f"src/assets/map_france_{self.selected_dimension.get()}.gif"))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Draw the cities ovals (for the normal cities)
        for city, coords in self.cities_data.items():
            is_highlighted = city in self.highlighted

            color = "#0000FF" if is_highlighted else "#FF0000"
            radius = 15 if is_highlighted else 10

            oval = self.draw_oval(coords["x"], coords["y"], radius, color, 1)
            self.canvas.tag_bind(oval, "<Button-1>", self.on_click_city(city))

            # Show a text of the city is "clicked"
            if self.clicked_city == city:
                self.canvas.create_text(coords["x"], coords["y"] - 15, text=city, fill="#000000")

    def on_click_city(self, city: str):
        def core(_event):
            if self.game:
                self.game.play(city)

            self.clicked_city = city
            self.draw_canvas()

        return core

    def on_update_selected_dimension(self, _, __, ___):
        self.draw_canvas()

    def on_update_selected_city(self, _, __, ___):
        self.highlighted = [self.selected_city.get()]
        self.draw_canvas()

    def add_listeners(self):
        self.selected_city.trace("w", self.on_update_selected_city)
        self.selected_dimension.trace("w", self.on_update_selected_dimension)

    def start_game(self):
        def core():
            def stop():
                self.game = None

            self.game = Game(self.cities_name, stop)
            self.game.start()

        return core

    def setup(self):
        # Create the add city button
        add_city_button = tk.Button(self.root, text="Ajouter une nouvelle ville", command=add_city_window)
        add_city_button.pack()

        # Create the dimensions dropdown
        dimensions_dropdown = tk.OptionMenu(self.root, self.selected_dimension, *self.available_dimensions)
        dimensions_dropdown.pack()

        # Create the cities dropdown
        cities_dropdown = tk.OptionMenu(self.root, self.selected_city, *self.cities_name)
        cities_dropdown.pack()

        # Create the start game button
        start_game_button = tk.Button(self.root, text='Jouer', command=self.start_game())
        start_game_button.pack()

        # Calculate distance button
        calc_dist_button = tk.Button(
            self.root,
            text="Calculer une distance",
            command=lambda: calc_dist_window(self.parsed_cities),
        )
        calc_dist_button.pack()

    def start(self):
        self.setup()
        self.add_listeners()
        self.draw_canvas()
        self.root.mainloop()


if __name__ == '__main__':
    instance = CitiesWindow()
    instance.start()
