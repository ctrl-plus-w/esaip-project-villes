from google_images_search import GoogleImagesSearch 
from PIL import Image
import requests
from io import BytesIO

def get_city_image(city_name):
    # Remplacez "VOTRE_CLE_API" par votre clé API Google
    gis = GoogleImagesSearch("AIzaSyB49sGb6ogwrx4sEBN5Hup4EDMd08gOYGc", "653363512392247ac")

    # Paramètres de la recherche
    search_params = {
        'q': f'{city_name} city',
        'num': 1,  # Vous pouvez ajuster le nombre d'images que vous souhaitez obtenir
        'safe': 'high',
        'fileType': 'jpg',
    }

    # Faire la recherche d'images
    gis.search(search_params=search_params)

    # Récupérer l'URL de l'image
    image_url = gis.results()[0].url

    # Télécharger et afficher l'image
    response_image = requests.get(image_url)
    image = Image.open(BytesIO(response_image.content))
    image.show()

# Exemple d'utilisation
city_name = "Paris"  # Remplacez par le nom de la ville souhaité
get_city_image(city_name)
