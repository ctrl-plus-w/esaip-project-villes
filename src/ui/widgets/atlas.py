from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class AtlasWidget( QWidget ):
    
    def __init__( self, villes: list ) -> None: 

        super( QWidget, self ).__init__()

        # layout
        self.layout = QGridLayout()
        self.setLayout( self.layout )

        # Town seleector
        self.town_label = QLabel( "Ville: " )

        self.town_selector = QComboBox()

        for ville in villes:
            self.town_selector.addItem( ville )

        # Add 2 layout
        self.layout.addWidget( self.town_label, 0, 0)
        self.layout.addWidget( self.town_selector, 0, 1 )
    
    def get_size( self ):
        return self.interface_selector.currentText()