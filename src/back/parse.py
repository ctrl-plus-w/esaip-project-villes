from scipy.interpolate import interp1d


def parse_cities(path: str):
    with open(path, 'r') as file:
        villes_coords = {}

        for line in file:
            name = line[:30].strip()
            lat = line[30:36]
            lng = line[53:63]

            villes_coords[name] = {"lat": float(lat), "lng": float(lng)}

    return villes_coords


def get_cities_as_coordinates(cities):
    cities["NorthWest"] = ({"lat": 52, "lng": -5.5})
    cities["SouthEst"] = ({"lat": 41, "lng": 10.5})

    lats = list(map(lambda c: c["lat"], cities.values()))
    lngs = list(map(lambda c: c["lng"], cities.values()))

    min_lat = min(lats)
    max_lat = max(lats)
    min_lng = min(lngs)
    max_lng = max(lngs)

    scale_y = interp1d([min_lat, max_lat], [494, 0])
    scale_x = interp1d([min_lng, max_lng], [0, 516])

    for city, coords in cities.items():
        y = scale_y(coords["lat"])
        x = scale_x(coords["lng"])

        cities[city] = {"x": x, "y": y, **coords}

    return cities
