import os
from typing import Dict

from scipy.interpolate import interp1d


def get_available_city_files():
    """
    Récupère les fichiers disponibles pour les villes.
    """
    filenames = os.listdir('src/assets')
    filenames = list(filter(lambda f: f.endswith('.gif'), filenames))

    def get_size(name: str):
        name = name.split('_')[-1]
        name = name.split('.')[0]

        width, height = name.split('x')
        return int(width), int(height)

    return list(map(lambda f: ({
        "filename": f,
        "label": 'x'.join(list(map(str, get_size(f)))), "width": get_size(f)[0],
        "height": get_size(f)[1]
    }), filenames))


def parse_cities(path: str):
    """
    Récupère les données associées aux villes du fichier au chemin donné dans les paramètres.

    :param path: Le chemin du fichier à parser.
    """
    with open(path, 'r') as file:
        villes_coords = {}

        for line in file:
            name = line[:30].strip()
            lat = line[30:36]
            lng = line[53:63]

            villes_coords[name] = {"lat": float(lat), "lng": float(lng)}

        villes_coords["NorthWest"] = ({"lat": 52, "lng": -5.5})
        villes_coords["SouthEst"] = ({"lat": 41, "lng": 10.5})

    return villes_coords


def get_min_max_lat_lng(cities: list[Dict[str, int]]):
    """
    Retourne le minimum et le maximum de la latitude et de la longitude.

    :param cities: La liste des villes (dictionnaires avec lat et lng)
    """
    lats = list(map(lambda c: c["lat"], cities.values()))
    lngs = list(map(lambda c: c["lng"], cities.values()))

    min_lat = min(lats)
    max_lat = max(lats)
    min_lng = min(lngs)
    max_lng = max(lngs)

    return min_lat, max_lat, min_lng, max_lng


def is_valid(cities, lat: float, lng: float) -> bool:
    """
    Vérifie que les coordonnées passées en paramètres sont valides.

    :param cities: La liste des villes (dictionnaires avec lat et lng)
    :param lat: La latitude des coordonnées.
    :param lng: Lat longitude des coordonnées.
    """
    min_lat, max_lat, min_lng, max_lng = get_min_max_lat_lng(cities)
    return min_lat <= lat <= max_lat and min_lng <= lng <= max_lng


def get_cities_as_coordinates(cities, width: int, height: int) -> dict:
    """
    Retourne la liste des villes avec les coordonnées (x et y) associés à la carte.

    :param cities: La liste des villes (dictionnaires avec lat et lng)
    :param width: La largeur de la canvas.
    :param height: La hauteur de la canvas.
    """
    min_lat, max_lat, min_lng, max_lng = get_min_max_lat_lng(cities)

    scale_y = interp1d([min_lat, max_lat], [width, 0])
    scale_x = interp1d([min_lng, max_lng], [0, height])

    for city, coords in cities.items():
        y = scale_y(coords["lat"])
        x = scale_x(coords["lng"])

        cities[city] = {"x": x, "y": y, **coords}

    return cities
