from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DimensionWidget( QWidget ):
    
    def __init__(self):

        super( QWidget, self ).__init__()

        # layout
        self.layout = QGridLayout()
        self.setLayout( self.layout )

        # Town seleector
        self.town_label = QLabel("Interface: ")

        self.town_selector = QComboBox()
        self.town_selector.addItem("496x516")
        self.town_selector.addItem("742x773")
        self.town_selector.addItem("989x1031")
        self.town_selector.addItem("1236x1289")

        # Add 2 layout
        self.layout.addWidget( self.town_label, 0, 0)
        self.layout.addWidget( self.town_selector, 0, 1 )
    
    def get_size( self ) -> list:
        return list(map(int, self.interface_selector.currentText().split("x")))