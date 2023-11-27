from geopy.distance import geodesic

def calculate_distance(coord1, coord2):
    """This function with 2 tuples of latitude and longitude can return the distance between
    example : (48.8566, 2.3522) and (40.7128, -74.0060)"""
    distance = geodesic(coord1, coord2).kilometers
    return distance

