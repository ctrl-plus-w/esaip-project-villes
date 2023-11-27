from parse import parse_cities
from random import choice
from find_city import find_city_with_coordonates

class Game:

    def __init__( self ):

        self.coups_restants = 20
        self.score = 0

        self.villes = parse_cities( "../assets/villes.txt" )

    def play_round( self ):
        liste = list ( self.villes.keys() )
        self.ville = choice( liste )

        self.coups_restants -= 1

        return self.ville

    def check_answer( self, coords_clique ) -> bool:

        city = find_city_with_coordonates( coords_clique[ 0 ], coords_clique[ 1 ] )

        if city == self.ville:
            self.score += 1
            return True
        
        return False

    def status( self ) -> dict:

        info = {
            "coups_restants" : self.coups_restants,
            "score" : self.score,
            "last_city" : self.ville
        }

        return info
    
game = Game()
game.play_round()
