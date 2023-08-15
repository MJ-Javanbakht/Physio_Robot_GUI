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

import sys
import os
import platform
from threading import Thread
from time import sleep

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.driveStarted = False
        # node = check_node() 
        self.network, self.drive = connect_node(1)
        init_drive(self.drive, 0.005)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "FUM - Physio"
        description = "FUM - Physio"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Make lineEdits accept only numbers
        # ///////////////////////////////////////////////////////////////
        lineEdits = widgets.stackedWidget.findChildren(QLineEdit)
        for l in lineEdits:
            l.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9]+')))
        
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_Homing.clicked.connect(self.buttonClick)
        widgets.btn_Passive.clicked.connect(self.buttonClick)
        widgets.btn_Isometric.clicked.connect(self.buttonClick)
        widgets.btn_Isotonic.clicked.connect(self.buttonClick)
        widgets.btn_Isokinetic.clicked.connect(self.buttonClick)
        widgets.btn_Spring.clicked.connect(self.buttonClick)
        widgets.btn_Water.clicked.connect(self.buttonClick)
        widgets.homingRun.clicked.connect(self.buttonClick)
        widgets.passiveRun.clicked.connect(self.buttonClick)
        widgets.IsometricRun.clicked.connect(self.buttonClick)
        widgets.isotonicRun.clicked.connect(self.buttonClick)
        
        # EXTRA LEFT BOX
        # def openCloseLeftBox():
        #     UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.Passive)
        widgets.btn_Passive.setStyleSheet(UIFunctions.selectMenu(widgets.btn_Passive.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW Homing PAGE
        if btnName == "btn_Homing":
            widgets.stackedWidget.setCurrentWidget(widgets.Homing)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # Run Homing
        if btnName == "homingRun":
            if not self.driveStarted:
                homing = Homing()
                homing.Home(self.drive)


        # SHOW Passive PAGE
        if btnName == "btn_Passive":
            widgets.stackedWidget.setCurrentWidget(widgets.Passive)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # Run Passive
        if btnName == "passiveRun":
            time = widgets.lineEdit_PassiveTime.text()
            restTime = widgets.lineEdit_PassiveRestTime.text()
            sets = widgets.lineEdit_PassiveSet.text()
            repeats = widgets.lineEdit_PassiveRepeat.text()
            minROM = widgets.lineEdit_PassiveMinROM.text()
            maxROM = widgets.lineEdit_PassiveMaxROM.text()
            speed = widgets.lineEdit_PassiveSpeed.text()
            p = Passive(time,restTime,sets,repeats,minROM,maxROM,speed)
            p.print()
        
        # SHOW Isometric PAGE
        if btnName == "btn_Isometric":
            widgets.stackedWidget.setCurrentWidget(widgets.Isometric)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # Run Isometric
        if btnName == "IsometricRun":
            Rest_Time =  int(widgets.lineEdit_IsometricRestTime.text())
            sets = int(widgets.lineEdit_IsometricSet.text())
            repeats = int(widgets.lineEdit_IsometricRepeat.text())
            force = int(widgets.lineEdit_IsometricForce.text())
            Hold_Time = int(widgets.lineEdit_IsometricHoldTime.text())
            pos1 = int(widgets.lineEdit_IsometricPos1.text())
            pos2 = int(widgets.lineEdit_IsometricPos2.text())
            pos3 = int(widgets.lineEdit_IsometricPos3.text())
            iso = Isometric()
            iso.run(self.drive, Rest_Time,sets,repeats,force,Hold_Time,pos1,pos2,pos3)

        # SHOW Isotonic PAGE
        if btnName == "btn_Isotonic":
            widgets.stackedWidget.setCurrentWidget(widgets.Isotonic)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # Run Isotonic
        if btnName == "isotonicRun":
            Rest_Time =  int(widgets.lineEdit_IsotonicRestTime.text())
            sets = int(widgets.lineEdit_IsotonicSet.text())
            repeats = int(widgets.lineEdit_IsotonicRepeat.text())
            extensionForce = int(widgets.lineEdit_IsotonicExtensionForce.text())
            flexionForce = int(widgets.lineEdit_IsotonicFlexionForce.text())
            minROM = int(widgets.lineEdit_IsotonicMinROM.text())
            maxROM = int(widgets.lineEdit_IsotonicMaxROM.text())
            # sleep(5)
            self.drive.sdo['Modes of operation'].raw = 4
            game = Game()
            game.start()
            p = Thread(target=game.run , args=(self.drive, maxROM-minROM))
            print(1)
            p.start()
            # p.join()
            # game.run(self.drive, maxROM - minROM)
            run(self.drive, Rest_Time, sets, repeats, extensionForce, flexionForce, minROM, maxROM)
        
        # SHOW Isokinetic PAGE
        if btnName == "btn_Isokinetic":
            widgets.stackedWidget.setCurrentWidget(widgets.Isokinetic)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # SHOW Spring Form PAGE
        if btnName == "btn_Spring":
            widgets.stackedWidget.setCurrentWidget(widgets.Spring)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # SHOW Water Form PAGE
        if btnName == "btn_Water":
            widgets.stackedWidget.setCurrentWidget(widgets.Water)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # # SHOW NEW PAGE
        # if btnName == "btn_new":
        #     widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
        #     UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
        #     btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.current_position = event.globalPos()
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.MouseButton.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.MouseButton.RightButton:
            print('Mouse click: RIGHT CLICK')

    def close(self) -> bool:
        self.drive.sdo['Controlword'].raw = 0
        self.network.disconnect()
        return super().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(app)
    window = MainWindow()
    print(window)
    sys.exit(app.exec())
