def parsing(path: str):
    with open(path, 'r') as file:
        villes_coords = {}
        for line in file:
            data = line.split()
            ville = data[0]
            coord1 = data[1]
            coord3 = data[4]
            villes_coords[ville] = (coord1, coord3)

    return villes_coords

