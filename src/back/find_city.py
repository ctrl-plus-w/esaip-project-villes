from parse import parsing

def find_city(city):
    dictionnaire = parsing("src/assets/villes.txt")
    if city in dictionnaire:
        return dictionnaire[city]['lat'],dictionnaire[city]['lng']
    else:
        return "Ville introuvable dans le dictionnaire"

