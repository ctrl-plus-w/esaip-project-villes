def split_coords(coords: str):
    """
    Convertie des coordonnées en format (48° 22'N)
    en un tuple avec de la forme '48' '22' 'N'.
    """
    degrees, reste = coords.split("° ")
    minutes, direction = reste.split("'")
    return degrees, minutes, direction


def convert(coords: str):
    """
    Convertie les coordonnées en format string en coordonnées en format décimal.
    """
    degrees, minutes, direction = split_coords(coords)

    if direction in ['N', 'E']:
        decimal = float(degrees) + float(minutes) / 60
    else:
        decimal = - (float(degrees) + float(minutes) / 60)

    return round(decimal, 3)


def add_city(name: str, latitude: str, longitude: str):
    """
    Ajoute dans le fichier 'villes.txt' une ville avec le nom, la latitude et la longitude passée en paramètres.
    """
    latitude_decimal = convert(latitude)
    longitude_decimal = convert(longitude)

    with open('src/assets/villes.txt', 'a') as file:
        file.write(
            f"{name.ljust(30)}{str(latitude_decimal).ljust(10)}{latitude.ljust(16)}{str(longitude_decimal).ljust(11)}{longitude}\n")

    print(f"Les coordonnées pour la ville de {name} ont été ajoutées au fichier.")
