def parsing(path: str):
    with open(path, 'r') as file:
        villes_coords = {}

        for line in file:
            name = line[:30].strip()
            lat = line[30:36]
            lng = line[53:63]

            villes_coords[name] = {"lat": float(lat), "lng": float(lng)}

    return villes_coords
