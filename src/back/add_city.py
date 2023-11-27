
def split_coordonnees(coordonnees):
    """This function parse coordonate string (48° 22'N) in to '48' '22' 'N'"""
    degres, reste = coordonnees.split("° ")
    minutes, direction = reste.split("'")
    return degres, minutes, direction

def convert(coordonnees):
    """This fuction convert string coordonate in to decimal coordonate"""
    degres, minutes, direction = split_coordonnees(coordonnees)
    if direction in ['N', 'E']:
        decimal = float(degres) + float(minutes) / 60
    else:
        decimal = - (float(degres) + float(minutes) / 60)

    return round(decimal, 3)

def add_city(ville, latitude, longitude):
    """This function write at the end of 'villes.txt' a new city with coordonate"""
    latitude_decimal = convert(latitude)
    longitude_decimal = convert(longitude)

    with open('src/assets/villes.txt', 'a') as file:
        file.write(f"{ville.ljust(30)}{str(latitude_decimal).ljust(10)}{latitude.ljust(16)}{str(longitude_decimal).ljust(11)}{longitude}\n")

    print(f"Les coordonnées pour la ville de {ville} ont été ajoutées au fichier.")