# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# GUI FILE
from . ui_main import Ui_MainWindow
from . test import Ui_MainWindow1

# APP SETTINGS
from . app_settings import Settings

# IMPORT FUNCTIONS
from . ui_functions import *

# APP FUNCTIONS
from . app_functions import *

# Moves
from modules.Moves.loadcell import loadcell
from modules.Moves.passive import *
from modules.Moves.Isometric import Isometric
from modules.Moves.Isotonic import *
# from Moves import *

# CanOpen
from modules.canOpen.check_node import *
from modules.canOpen.config import *
from modules.canOpen.Homing import *
from modules.canOpen.Position import *
from modules.canOpen.Tourqe import *
from modules.canOpen.Velocity import *

# Games
from modules.games.Flappy_game import Game