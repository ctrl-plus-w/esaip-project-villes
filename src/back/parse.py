def parsing(path: str):
    with open(path, 'r') as file:
        villes_coords = {}

        for line in file:
            data = line.split()
            ville = data[0]

            lat = data[1]
            lng = data[4]

            villes_coords[ville] = {"lat": lat, "lng": lng}

    return villes_coords
