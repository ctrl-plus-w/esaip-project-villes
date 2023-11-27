from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

class ImageWidget( QWidget ):
    
    def __init__( self, image_path ):

        super( QWidget, self ).__init__()

        self.lb = QLabel( self )
        pixmap = QPixmap( image_path )

        self.lb.resize( self.width(), self.height() )
        self.lb.setPixmap( pixmap.scaled( self.lb.size(), Qt.IgnoreAspectRatio ) )
        #self.show()