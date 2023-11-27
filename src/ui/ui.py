import PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

from src.ui.widgets.taille



    """
    Main window
    """
class VilleClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(

        # initialize the window information with the title and screen size
        self.setWindowTitle( 'Imperium: Client' );
        self.setGeometry( 0, 0, int(screen_width / 4), int(screen_height / 4))

        # Center of the screen
        screen = QApplication.desktop().screenGeometry()
        x = ( screen.width() - self.width() ) // 2
        y = ( screen.height() - self.height() ) // 2
        self.move(x, y)
        # Taille 
        self.taille = TailleWidget()

        # Widget
        widget = QWidget()
        self.setCentralWidget( widget )

        layout = QVBoxLayout()
        widget.setLayout( layout )
        layout.addWidget( self.taille )            0,
        )
