from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

class ImageWidget( QWidget ):
    
    def __init__( self, image_path, width, height ):

        super( QWidget, self ).__init__()

        self.lb = QLabel( self )
        pixmap = QPixmap( image_path )

        self.lb.resize( width, height )
        self.lb.setPixmap( pixmap.scaled( width, height ) )


        self.print_point( [ 100, 100 ] )
        self.print_point( [ 200, 200 ] )
        self.print_point( [ 300, 300 ] )
    
    def print_point( self, coords ) -> None:
        """
        Print a point on the image.
        Coords is a list of 2 elements, the first is the x coordinate and the second is the y coordinate.
        """
        
        self.p = QPoint()

        self.p.setX( coords[ 0 ] )
        self.p.setY( coords[ 1 ] )