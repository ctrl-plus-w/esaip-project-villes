import random
import tkinter as tk


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
        """
        Réinitialise les propriétés de la game.
        """
        self.available_cities = self.default_available_cities
        self.remaining_plays = self.total_plays
        self.score = 0

        self.seeked_city = random.choice(self.available_cities)
        self.draw_game()

    def draw_game(self):
        """
        Dessine la fenêtre du jeu.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

        # S'il ne reste plus de coups à jouer
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

        # S'il reste des coups à jouer
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
        """
        Joue un coup dans la partie du jeu.

        :param city: Le nom de la ville jouée.
        """
        if city == self.seeked_city:
            self.score += 1

        # Decrement the total of remaining plays
        self.remaining_plays -= 1

        # Removed the city from the available cities and update the seeked city randomly
        self.available_cities.remove(self.seeked_city)
        self.seeked_city = random.choice(self.available_cities)

        self.draw_game()

    def start(self):
        """
        Lance la partie.
        """
        self.draw_game()

    def quit(self):
        """
        Termine la partie.
        """
        self.root.destroy()
        self.stop()
