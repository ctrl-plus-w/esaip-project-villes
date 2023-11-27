from parse import parsing

def find_city(city):
    """This function look for a city and return lat and lng if found"""
    dictionnaire = parsing("src/assets/villes.txt")
    if city in dictionnaire:
        return dictionnaire[city]
    else:
        raise Exception

def find_city_with_coordonates(lat, lng):
    dictionnaire = parsing("src/assets/villes.txt")
    for key in dictionnaire:
        if dictionnaire[key]["lat"] == lat and dictionnaire[key]["lng"] == lng:
            return key
    return {}

