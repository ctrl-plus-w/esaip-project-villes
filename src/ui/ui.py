
import qdarktheme, sys
from src.ui.widgets.dimension import DimensionWidget
from src.ui.widgets.add_town import AddTownWidget
from src.ui.widgets.image import ImageWidget

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow( QMainWindow ):
    """ Main window"""

    def __init__( self, screen_width, screen_height ):
        # init the primary QMainWindow class
        super().__init__()

        # initialize the window information with the title and screen size
        self.setWindowTitle( 'Villes: Client' );
        self.setGeometry( 0, 0, int( screen_width / 4 ), int( screen_height / 4 ) )

        # Center of the screen
        screen = QApplication.desktop().screenGeometry()
        x = ( screen.width() - self.width() ) // 2
        y = ( screen.height() - self.height() ) // 2
        self.move(x, y)

        # Dimension
        self.dimension = DimensionWidget()
        self.add_town = AddTownWidget()
        self.image = ImageWidget( "src/assets/map_france_494x516.gif", 496, 516 )

        # Widget
        widget = QWidget()
        self.setCentralWidget( widget )

        layout = QVBoxLayout()
        widget.setLayout( layout )
        #layout.addWidget( self.add_town )
        layout.addWidget( self.image )

def main():
    """
    Entry for the client, make the login window appear.
    """

    app = QApplication( [ ] )

    # Load theme
    app.setStyleSheet( qdarktheme.load_stylesheet() );
    
    # Init window
    window = MainWindow( app.primaryScreen().size().height(), app.primaryScreen().size().width() )
    window.show()

    sys.exit( app.exec_() )
