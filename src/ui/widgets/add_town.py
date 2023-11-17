from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class AddTownWidget( QWidget ):
    
    def __init__(self):

        super( QWidget, self ).__init__()

        # layout
        self.layout = QGridLayout()
        self.setLayout( self.layout )

        # Insert town name
        self.town_label = QLabel( "Nom de la ville: " )
        self.town_prompt = QLineEdit()
        self.layout.addWidget( self.town_label, 0, 0 )
        self.layout.addWidget( self.town_prompt, 0, 1)

        # Insert latitude
        self.latitude_label1 = QLabel( "Latitude: ")
        self.latitude_prompt1 = QLineEdit()
        self.latitude_label2 = QLabel( "°")
        self.latitude_prompt2 = QLineEdit()
        self.latitude_label3 = QLabel( "'N" )
        self.layout.addWidget( self.latitude_label1 , 1, 0 )
        self.layout.addWidget( self.latitude_prompt1, 1, 1 )
        self.layout.addWidget( self.latitude_label2 , 1, 2 )
        self.layout.addWidget( self.latitude_prompt2, 1, 3 )
        self.layout.addWidget( self.latitude_label3, 1, 4 )

        # Insert longitude
        self.longitude_label1 = QLabel( "Longitude: ")
        self.longitude_prompt1 = QLineEdit()
        self.longitude_label2 = QLabel( "°")
        self.longitude_prompt2 = QLineEdit()
        self.longitude_selector = QComboBox()
        self.longitude_selector.addItem("'W")
        self.longitude_selector.addItem("'E")

        self.layout.addWidget( self.longitude_label1  , 2, 0 )
        self.layout.addWidget( self.longitude_prompt1 , 2, 1 )
        self.layout.addWidget( self.longitude_label2  , 2, 2 )
        self.layout.addWidget( self.longitude_prompt2 , 2, 3 )
        self.layout.addWidget( self.longitude_selector, 2, 5 )
        
        self.save_button = QPushButton( "Save" )
        self.save_button.clicked.connect( self.save )
        self.layout.addWidget( self.save_button, 3, 0 )

    def save( self ):
        pass