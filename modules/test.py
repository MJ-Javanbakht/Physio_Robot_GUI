# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainOYKsRP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .resources_rc import *

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 16pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/logofumcare01.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 10px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rg"
                        "b(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: "
                        "rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	bo"
                        "rder-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border"
                        "-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 12px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color:"
                        " rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	backgroun"
                        "d-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(20, 20, 20);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-backgrou"
                        "nd-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
" "
                        "    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
""
                        "	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	"
                        "subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
""
                        "    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QComm"
                        "andLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(220, 0))
        self.leftMenuBg.setMaximumSize(QSize(220, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 60))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 60))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 210, 60))
        self.topLogo.setMinimumSize(QSize(210, 60))
        self.topLogo.setMaximumSize(QSize(210, 60))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_Homing = QPushButton(self.topMenu)
        self.btn_Homing.setObjectName(u"btn_Homing")
        self.btn_Homing.setMinimumSize(QSize(0, 45))
        self.btn_Homing.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-home.png);*/\n"
"border-bottom: 1px solid rgb(40, 44, 52);")

        self.verticalLayout_8.addWidget(self.btn_Homing)

        self.btn_Passive = QPushButton(self.topMenu)
        self.btn_Passive.setObjectName(u"btn_Passive")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Passive.sizePolicy().hasHeightForWidth())
        self.btn_Passive.setSizePolicy(sizePolicy)
        self.btn_Passive.setMinimumSize(QSize(0, 45))
        self.btn_Passive.setFont(font)
        self.btn_Passive.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Passive.setLayoutDirection(Qt.LeftToRight)
        self.btn_Passive.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-home.png);*/\n"
"border-bottom: 1px solid rgb(40, 44, 52);")

        self.verticalLayout_8.addWidget(self.btn_Passive)

        self.btn_Isometric = QPushButton(self.topMenu)
        self.btn_Isometric.setObjectName(u"btn_Isometric")
        sizePolicy.setHeightForWidth(self.btn_Isometric.sizePolicy().hasHeightForWidth())
        self.btn_Isometric.setSizePolicy(sizePolicy)
        self.btn_Isometric.setMinimumSize(QSize(0, 45))
        self.btn_Isometric.setFont(font)
        self.btn_Isometric.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Isometric.setLayoutDirection(Qt.LeftToRight)
        self.btn_Isometric.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-gamepad.png);*/\n"
"border-bottom: 1px solid rgb(40, 44, 52);")

        self.verticalLayout_8.addWidget(self.btn_Isometric)

        self.btn_Isotonic = QPushButton(self.topMenu)
        self.btn_Isotonic.setObjectName(u"btn_Isotonic")
        sizePolicy.setHeightForWidth(self.btn_Isotonic.sizePolicy().hasHeightForWidth())
        self.btn_Isotonic.setSizePolicy(sizePolicy)
        self.btn_Isotonic.setMinimumSize(QSize(0, 45))
        self.btn_Isotonic.setFont(font)
        self.btn_Isotonic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Isotonic.setLayoutDirection(Qt.LeftToRight)
        self.btn_Isotonic.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-file.png);*/\n"
"border-bottom: 1px solid rgb(40, 44, 52);")

        self.verticalLayout_8.addWidget(self.btn_Isotonic)

        self.btn_Isokinetic = QPushButton(self.topMenu)
        self.btn_Isokinetic.setObjectName(u"btn_Isokinetic")
        sizePolicy.setHeightForWidth(self.btn_Isokinetic.sizePolicy().hasHeightForWidth())
        self.btn_Isokinetic.setSizePolicy(sizePolicy)
        self.btn_Isokinetic.setMinimumSize(QSize(0, 45))
        self.btn_Isokinetic.setFont(font)
        self.btn_Isokinetic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Isokinetic.setLayoutDirection(Qt.LeftToRight)
        self.btn_Isokinetic.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-exit-to-app.png);*/\n"
"border-bottom: 1px solid rgb(40, 44, 52);")

        self.verticalLayout_8.addWidget(self.btn_Isokinetic)

        self.btn_Spring = QPushButton(self.topMenu)
        self.btn_Spring.setObjectName(u"btn_Spring")
        sizePolicy.setHeightForWidth(self.btn_Spring.sizePolicy().hasHeightForWidth())
        self.btn_Spring.setSizePolicy(sizePolicy)
        self.btn_Spring.setMinimumSize(QSize(0, 45))
        self.btn_Spring.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Spring.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-vertical-align-bottom.png);*/\n"
"border-bottom: 1px solid rgb(40, 44, 52);")

        self.verticalLayout_8.addWidget(self.btn_Spring)

        self.btn_Water = QPushButton(self.topMenu)
        self.btn_Water.setObjectName(u"btn_Water")
        sizePolicy.setHeightForWidth(self.btn_Water.sizePolicy().hasHeightForWidth())
        self.btn_Water.setSizePolicy(sizePolicy)
        self.btn_Water.setMinimumSize(QSize(0, 45))
        self.btn_Water.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Water.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-chevron-double-up.png);*/\n"
"border-bottom: 1px solid rgb(40, 44, 52);")

        self.verticalLayout_8.addWidget(self.btn_Water)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"/*background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 60))
        self.contentTopBg.setMaximumSize(QSize(16777215, 60))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.Homing = QWidget()
        self.Homing.setObjectName(u"Homing")
        self.gridLayout_Homing = QGridLayout(self.Homing)
        self.gridLayout_Homing.setSpacing(10)
        self.gridLayout_Homing.setObjectName(u"gridLayout_Homing")
        self.gridLayout_Homing.setContentsMargins(100, 10, 100, 10)
        self.homingRun = QPushButton(self.Homing)
        self.homingRun.setObjectName(u"homingRun")
        self.homingRun.setMinimumSize(QSize(150, 45))
        self.homingRun.setStyleSheet(u"QPushButton{\n"
"	color: rgb(150, 200, 150);\n"
"	background-color: rgb(0, 120, 0);\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(0,100,0);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"")

        self.gridLayout_Homing.addWidget(self.homingRun, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.text_Homing = QTextBrowser(self.Homing)
        self.text_Homing.setObjectName(u"text_Homing")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.text_Homing.setFont(font3)
        self.text_Homing.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgb(27, 29, 35);\n"
"	color: green;\n"
"	font: 12px;\n"
"}")
        self.text_Homing.setFrameShape(QFrame.NoFrame)
        self.text_Homing.setFrameShadow(QFrame.Sunken)
        self.text_Homing.setLineWidth(1)
        self.text_Homing.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.text_Homing.setOpenExternalLinks(True)

        self.gridLayout_Homing.addWidget(self.text_Homing, 1, 0, 1, 1)

        self.gridLayout_Homing.setRowMinimumHeight(0, 100)
        self.gridLayout_Homing.setRowMinimumHeight(1, 100)
        self.stackedWidget.addWidget(self.Homing)
        self.Passive = QWidget()
        self.Passive.setObjectName(u"Passive")
        self.Passive.setStyleSheet(u"")
        self.gridLayout_Passive = QGridLayout(self.Passive)
        self.gridLayout_Passive.setObjectName(u"gridLayout_Passive")
        self.gridLayout_Passive.setHorizontalSpacing(50)
        self.gridLayout_Passive.setVerticalSpacing(0)
        self.label_PassiveSet = QLabel(self.Passive)
        self.label_PassiveSet.setObjectName(u"label_PassiveSet")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_PassiveSet.sizePolicy().hasHeightForWidth())
        self.label_PassiveSet.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.label_PassiveSet, 2, 0, 1, 1)

        self.lineEdit_PassiveRepeat = QLineEdit(self.Passive)
        self.lineEdit_PassiveRepeat.setObjectName(u"lineEdit_PassiveRepeat")
        sizePolicy3.setHeightForWidth(self.lineEdit_PassiveRepeat.sizePolicy().hasHeightForWidth())
        self.lineEdit_PassiveRepeat.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.lineEdit_PassiveRepeat, 2, 3, 1, 1)

        self.label_PassiveSpeed = QLabel(self.Passive)
        self.label_PassiveSpeed.setObjectName(u"label_PassiveSpeed")
        sizePolicy3.setHeightForWidth(self.label_PassiveSpeed.sizePolicy().hasHeightForWidth())
        self.label_PassiveSpeed.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.label_PassiveSpeed, 4, 0, 1, 1)

        self.label_PassiveRestTime = QLabel(self.Passive)
        self.label_PassiveRestTime.setObjectName(u"label_PassiveRestTime")
        sizePolicy3.setHeightForWidth(self.label_PassiveRestTime.sizePolicy().hasHeightForWidth())
        self.label_PassiveRestTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.label_PassiveRestTime, 1, 2, 1, 1)

        self.lineEdit_PassiveSpeed = QLineEdit(self.Passive)
        self.lineEdit_PassiveSpeed.setObjectName(u"lineEdit_PassiveSpeed")
        sizePolicy3.setHeightForWidth(self.lineEdit_PassiveSpeed.sizePolicy().hasHeightForWidth())
        self.lineEdit_PassiveSpeed.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.lineEdit_PassiveSpeed, 4, 1, 1, 1)

        self.lineEdit_PassiveMaxROM = QLineEdit(self.Passive)
        self.lineEdit_PassiveMaxROM.setObjectName(u"lineEdit_PassiveMaxROM")
        sizePolicy3.setHeightForWidth(self.lineEdit_PassiveMaxROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_PassiveMaxROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.lineEdit_PassiveMaxROM, 3, 3, 1, 1)

        self.label_PassiveMinROM = QLabel(self.Passive)
        self.label_PassiveMinROM.setObjectName(u"label_PassiveMinROM")
        sizePolicy3.setHeightForWidth(self.label_PassiveMinROM.sizePolicy().hasHeightForWidth())
        self.label_PassiveMinROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.label_PassiveMinROM, 3, 0, 1, 1)

        self.lineEdit_PassiveRestTime = QLineEdit(self.Passive)
        self.lineEdit_PassiveRestTime.setObjectName(u"lineEdit_PassiveRestTime")
        sizePolicy3.setHeightForWidth(self.lineEdit_PassiveRestTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_PassiveRestTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.lineEdit_PassiveRestTime, 1, 3, 1, 1)

        self.lineEdit_PassiveMinROM = QLineEdit(self.Passive)
        self.lineEdit_PassiveMinROM.setObjectName(u"lineEdit_PassiveMinROM")
        sizePolicy3.setHeightForWidth(self.lineEdit_PassiveMinROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_PassiveMinROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.lineEdit_PassiveMinROM, 3, 1, 1, 1)

        self.label_PassiveMaxROM = QLabel(self.Passive)
        self.label_PassiveMaxROM.setObjectName(u"label_PassiveMaxROM")
        sizePolicy3.setHeightForWidth(self.label_PassiveMaxROM.sizePolicy().hasHeightForWidth())
        self.label_PassiveMaxROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.label_PassiveMaxROM, 3, 2, 1, 1)

        self.lineEdit_PassiveSet = QLineEdit(self.Passive)
        self.lineEdit_PassiveSet.setObjectName(u"lineEdit_PassiveSet")
        sizePolicy3.setHeightForWidth(self.lineEdit_PassiveSet.sizePolicy().hasHeightForWidth())
        self.lineEdit_PassiveSet.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.lineEdit_PassiveSet, 2, 1, 1, 1)

        self.label_PassiveTime = QLabel(self.Passive)
        self.label_PassiveTime.setObjectName(u"label_PassiveTime")
        sizePolicy3.setHeightForWidth(self.label_PassiveTime.sizePolicy().hasHeightForWidth())
        self.label_PassiveTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.label_PassiveTime, 1, 0, 1, 1)

        self.lineEdit_PassiveTime = QLineEdit(self.Passive)
        self.lineEdit_PassiveTime.setObjectName(u"lineEdit_PassiveTime")
        sizePolicy3.setHeightForWidth(self.lineEdit_PassiveTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_PassiveTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.lineEdit_PassiveTime, 1, 1, 1, 1)

        self.label_PassiveRepeat = QLabel(self.Passive)
        self.label_PassiveRepeat.setObjectName(u"label_PassiveRepeat")
        sizePolicy3.setHeightForWidth(self.label_PassiveRepeat.sizePolicy().hasHeightForWidth())
        self.label_PassiveRepeat.setSizePolicy(sizePolicy3)

        self.gridLayout_Passive.addWidget(self.label_PassiveRepeat, 2, 2, 1, 1)

        self.label_Passive = QLabel(self.Passive)
        self.label_Passive.setObjectName(u"label_Passive")
        sizePolicy3.setHeightForWidth(self.label_Passive.sizePolicy().hasHeightForWidth())
        self.label_Passive.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(30)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_Passive.setFont(font4)
        self.label_Passive.setStyleSheet(u"font: 30pt \"Segoe UI\";\n"
"color: rgb(170, 85, 255);")

        self.gridLayout_Passive.addWidget(self.label_Passive, 0, 0, 1, 4, Qt.AlignHCenter)

        self.passiveRun = QPushButton(self.Passive)
        self.passiveRun.setObjectName(u"passiveRun")
        self.passiveRun.setMinimumSize(QSize(100, 0))
        self.passiveRun.setStyleSheet(u"QPushButton{\n"
"	color: rgb(150, 200, 150);\n"
"	background-color: rgb(0, 120, 0);\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(0,100,0);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"")

        self.gridLayout_Passive.addWidget(self.passiveRun, 4, 2, 1, 2, Qt.AlignHCenter)

        self.gridLayout_Passive.setRowStretch(0, 1)
        self.gridLayout_Passive.setRowStretch(1, 2)
        self.gridLayout_Passive.setRowStretch(2, 2)
        self.gridLayout_Passive.setRowStretch(3, 2)
        self.gridLayout_Passive.setRowStretch(4, 2)
        self.gridLayout_Passive.setColumnStretch(0, 1)
        self.gridLayout_Passive.setColumnStretch(1, 2)
        self.gridLayout_Passive.setColumnStretch(2, 1)
        self.gridLayout_Passive.setColumnStretch(3, 2)
        self.stackedWidget.addWidget(self.Passive)
        self.Isometric = QWidget()
        self.Isometric.setObjectName(u"Isometric")
        self.gridLayout_Isometric = QGridLayout(self.Isometric)
        self.gridLayout_Isometric.setObjectName(u"gridLayout_Isometric")
        self.gridLayout_Isometric.setHorizontalSpacing(50)
        self.gridLayout_Isometric.setVerticalSpacing(0)
        self.label_IsometricTime = QLabel(self.Isometric)
        self.label_IsometricTime.setObjectName(u"label_IsometricTime")

        self.gridLayout_Isometric.addWidget(self.label_IsometricTime, 1, 0, 1, 1, Qt.AlignVCenter)

        self.groupBox_IsometricPos = QGroupBox(self.Isometric)
        self.groupBox_IsometricPos.setObjectName(u"groupBox_IsometricPos")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_IsometricPos.sizePolicy().hasHeightForWidth())
        self.groupBox_IsometricPos.setSizePolicy(sizePolicy4)
        self.groupBox_IsometricPos.setFlat(False)
        self.groupBox_IsometricPos.setCheckable(False)
        self.gridLayout_IsometricPos = QGridLayout(self.groupBox_IsometricPos)
        self.gridLayout_IsometricPos.setObjectName(u"gridLayout_IsometricPos")
        self.label_IsometricPos1 = QLabel(self.groupBox_IsometricPos)
        self.label_IsometricPos1.setObjectName(u"label_IsometricPos1")

        self.gridLayout_IsometricPos.addWidget(self.label_IsometricPos1, 0, 0, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricPos1 = QLineEdit(self.groupBox_IsometricPos)
        self.lineEdit_IsometricPos1.setObjectName(u"lineEdit_IsometricPos1")

        self.gridLayout_IsometricPos.addWidget(self.lineEdit_IsometricPos1, 0, 1, 1, 1, Qt.AlignVCenter)

        self.label_IsometricPos2 = QLabel(self.groupBox_IsometricPos)
        self.label_IsometricPos2.setObjectName(u"label_IsometricPos2")

        self.gridLayout_IsometricPos.addWidget(self.label_IsometricPos2, 1, 0, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricPos2 = QLineEdit(self.groupBox_IsometricPos)
        self.lineEdit_IsometricPos2.setObjectName(u"lineEdit_IsometricPos2")

        self.gridLayout_IsometricPos.addWidget(self.lineEdit_IsometricPos2, 1, 1, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricPos3 = QLineEdit(self.groupBox_IsometricPos)
        self.lineEdit_IsometricPos3.setObjectName(u"lineEdit_IsometricPos3")

        self.gridLayout_IsometricPos.addWidget(self.lineEdit_IsometricPos3, 2, 1, 1, 1, Qt.AlignVCenter)

        self.label_IsometricPos3 = QLabel(self.groupBox_IsometricPos)
        self.label_IsometricPos3.setObjectName(u"label_IsometricPos3")

        self.gridLayout_IsometricPos.addWidget(self.label_IsometricPos3, 2, 0, 1, 1, Qt.AlignVCenter)

        self.gridLayout_IsometricPos.setColumnStretch(0, 1)
        self.gridLayout_IsometricPos.setColumnStretch(1, 3)

        self.gridLayout_Isometric.addWidget(self.groupBox_IsometricPos, 3, 2, 2, 2)

        self.lineEdit_IsometricSet = QLineEdit(self.Isometric)
        self.lineEdit_IsometricSet.setObjectName(u"lineEdit_IsometricSet")

        self.gridLayout_Isometric.addWidget(self.lineEdit_IsometricSet, 2, 1, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricRestTime = QLineEdit(self.Isometric)
        self.lineEdit_IsometricRestTime.setObjectName(u"lineEdit_IsometricRestTime")

        self.gridLayout_Isometric.addWidget(self.lineEdit_IsometricRestTime, 1, 3, 1, 1, Qt.AlignVCenter)

        self.label_IsometricSet = QLabel(self.Isometric)
        self.label_IsometricSet.setObjectName(u"label_IsometricSet")

        self.gridLayout_Isometric.addWidget(self.label_IsometricSet, 2, 0, 1, 1, Qt.AlignVCenter)

        self.label_IsometricRestTime = QLabel(self.Isometric)
        self.label_IsometricRestTime.setObjectName(u"label_IsometricRestTime")

        self.gridLayout_Isometric.addWidget(self.label_IsometricRestTime, 1, 2, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricForce = QLineEdit(self.Isometric)
        self.lineEdit_IsometricForce.setObjectName(u"lineEdit_IsometricForce")

        self.gridLayout_Isometric.addWidget(self.lineEdit_IsometricForce, 3, 1, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricRepeat = QLineEdit(self.Isometric)
        self.lineEdit_IsometricRepeat.setObjectName(u"lineEdit_IsometricRepeat")

        self.gridLayout_Isometric.addWidget(self.lineEdit_IsometricRepeat, 2, 3, 1, 1, Qt.AlignVCenter)

        self.IsometricRun = QPushButton(self.Isometric)
        self.IsometricRun.setObjectName(u"IsometricRun")
        self.IsometricRun.setMinimumSize(QSize(100, 0))
        self.IsometricRun.setStyleSheet(u"QPushButton{\n"
"	color: rgb(150, 200, 150);\n"
"	background-color: rgb(0, 120, 0);\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(0,100,0);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"")

        self.gridLayout_Isometric.addWidget(self.IsometricRun, 6, 2, 1, 2, Qt.AlignHCenter)

        self.label_IsometricRepeat = QLabel(self.Isometric)
        self.label_IsometricRepeat.setObjectName(u"label_IsometricRepeat")

        self.gridLayout_Isometric.addWidget(self.label_IsometricRepeat, 2, 2, 1, 1, Qt.AlignVCenter)

        self.label_IsometricForce = QLabel(self.Isometric)
        self.label_IsometricForce.setObjectName(u"label_IsometricForce")

        self.gridLayout_Isometric.addWidget(self.label_IsometricForce, 3, 0, 1, 1, Qt.AlignVCenter)

        self.label_IsometricHoldTime = QLabel(self.Isometric)
        self.label_IsometricHoldTime.setObjectName(u"label_IsometricHoldTime")

        self.gridLayout_Isometric.addWidget(self.label_IsometricHoldTime, 4, 0, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricHoldTime = QLineEdit(self.Isometric)
        self.lineEdit_IsometricHoldTime.setObjectName(u"lineEdit_IsometricHoldTime")

        self.gridLayout_Isometric.addWidget(self.lineEdit_IsometricHoldTime, 4, 1, 1, 1, Qt.AlignVCenter)

        self.lineEdit_IsometricTime = QLineEdit(self.Isometric)
        self.lineEdit_IsometricTime.setObjectName(u"lineEdit_IsometricTime")

        self.gridLayout_Isometric.addWidget(self.lineEdit_IsometricTime, 1, 1, 1, 1, Qt.AlignVCenter)

        self.label_Isometric = QLabel(self.Isometric)
        self.label_Isometric.setObjectName(u"label_Isometric")
        sizePolicy3.setHeightForWidth(self.label_Isometric.sizePolicy().hasHeightForWidth())
        self.label_Isometric.setSizePolicy(sizePolicy3)
        self.label_Isometric.setStyleSheet(u"font: 30pt \"Segoe UI\";\n"
"color: rgb(170, 85, 255)")

        self.gridLayout_Isometric.addWidget(self.label_Isometric, 0, 0, 1, 4, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_Isometric.addItem(self.verticalSpacer, 5, 2, 1, 1)

        self.gridLayout_Isometric.setRowStretch(0, 1)
        self.gridLayout_Isometric.setRowStretch(1, 2)
        self.gridLayout_Isometric.setRowStretch(2, 2)
        self.gridLayout_Isometric.setRowStretch(3, 2)
        self.gridLayout_Isometric.setRowStretch(4, 2)
        self.gridLayout_Isometric.setColumnStretch(0, 1)
        self.gridLayout_Isometric.setColumnStretch(1, 2)
        self.gridLayout_Isometric.setColumnStretch(2, 1)
        self.gridLayout_Isometric.setColumnStretch(3, 2)
        self.stackedWidget.addWidget(self.Isometric)
        self.Isotonic = QWidget()
        self.Isotonic.setObjectName(u"Isotonic")
        self.gridLayout_Isotonic = QGridLayout(self.Isotonic)
        self.gridLayout_Isotonic.setObjectName(u"gridLayout_Isotonic")
        self.gridLayout_Isotonic.setHorizontalSpacing(50)
        self.gridLayout_Isotonic.setVerticalSpacing(0)
        self.lineEdit_IsotonicMinROM = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicMinROM.setObjectName(u"lineEdit_IsotonicMinROM")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicMinROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicMinROM.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicMinROM, 3, 1, 1, 1)

        self.lineEdit_IsotonicRepeat = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicRepeat.setObjectName(u"lineEdit_IsotonicRepeat")
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicRepeat.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicRepeat.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicRepeat, 2, 3, 1, 1)

        self.lineEdit_IsotonicTime = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicTime.setObjectName(u"lineEdit_IsotonicTime")
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicTime.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicTime, 1, 1, 1, 1)

        self.label_IsotonicFlexionForce = QLabel(self.Isotonic)
        self.label_IsotonicFlexionForce.setObjectName(u"label_IsotonicFlexionForce")
        sizePolicy3.setHeightForWidth(self.label_IsotonicFlexionForce.sizePolicy().hasHeightForWidth())
        self.label_IsotonicFlexionForce.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicFlexionForce, 4, 2, 1, 1)

        self.lineEdit_IsotonicRestTime = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicRestTime.setObjectName(u"lineEdit_IsotonicRestTime")
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicRestTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicRestTime.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicRestTime, 1, 3, 1, 1)

        self.label_IsotonicTime = QLabel(self.Isotonic)
        self.label_IsotonicTime.setObjectName(u"label_IsotonicTime")
        sizePolicy3.setHeightForWidth(self.label_IsotonicTime.sizePolicy().hasHeightForWidth())
        self.label_IsotonicTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicTime, 1, 0, 1, 1)

        self.lineEdit_IsotonicExtensionForce = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicExtensionForce.setObjectName(u"lineEdit_IsotonicExtensionForce")
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicExtensionForce.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicExtensionForce.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicExtensionForce, 4, 1, 1, 1)

        self.lineEdit_IsotonicFlexionForce = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicFlexionForce.setObjectName(u"lineEdit_IsotonicFlexionForce")
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicFlexionForce.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicFlexionForce.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicFlexionForce, 4, 3, 1, 1)

        self.label_IsotonicMaxROM = QLabel(self.Isotonic)
        self.label_IsotonicMaxROM.setObjectName(u"label_IsotonicMaxROM")
        sizePolicy3.setHeightForWidth(self.label_IsotonicMaxROM.sizePolicy().hasHeightForWidth())
        self.label_IsotonicMaxROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicMaxROM, 3, 2, 1, 1)

        self.label_IsotonicRestTime = QLabel(self.Isotonic)
        self.label_IsotonicRestTime.setObjectName(u"label_IsotonicRestTime")
        sizePolicy3.setHeightForWidth(self.label_IsotonicRestTime.sizePolicy().hasHeightForWidth())
        self.label_IsotonicRestTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicRestTime, 1, 2, 1, 1)

        self.lineEdit_IsotonicSet = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicSet.setObjectName(u"lineEdit_IsotonicSet")
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicSet.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicSet.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicSet, 2, 1, 1, 1)

        self.label_Isotonic = QLabel(self.Isotonic)
        self.label_Isotonic.setObjectName(u"label_Isotonic")
        sizePolicy3.setHeightForWidth(self.label_Isotonic.sizePolicy().hasHeightForWidth())
        self.label_Isotonic.setSizePolicy(sizePolicy3)
        self.label_Isotonic.setStyleSheet(u"font: 30pt \"Segoe UI\";\n"
"color: rgb(170, 85, 255);")

        self.gridLayout_Isotonic.addWidget(self.label_Isotonic, 0, 0, 1, 4, Qt.AlignHCenter)

        self.label_IsotonicSet = QLabel(self.Isotonic)
        self.label_IsotonicSet.setObjectName(u"label_IsotonicSet")
        sizePolicy3.setHeightForWidth(self.label_IsotonicSet.sizePolicy().hasHeightForWidth())
        self.label_IsotonicSet.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicSet, 2, 0, 1, 1)

        self.label_IsotonicMinROM = QLabel(self.Isotonic)
        self.label_IsotonicMinROM.setObjectName(u"label_IsotonicMinROM")
        sizePolicy3.setHeightForWidth(self.label_IsotonicMinROM.sizePolicy().hasHeightForWidth())
        self.label_IsotonicMinROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicMinROM, 3, 0, 1, 1)

        self.label_IsotonicRepeat = QLabel(self.Isotonic)
        self.label_IsotonicRepeat.setObjectName(u"label_IsotonicRepeat")
        sizePolicy3.setHeightForWidth(self.label_IsotonicRepeat.sizePolicy().hasHeightForWidth())
        self.label_IsotonicRepeat.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicRepeat, 2, 2, 1, 1)

        self.lineEdit_IsotonicMaxROM = QLineEdit(self.Isotonic)
        self.lineEdit_IsotonicMaxROM.setObjectName(u"lineEdit_IsotonicMaxROM")
        sizePolicy5.setHeightForWidth(self.lineEdit_IsotonicMaxROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_IsotonicMaxROM.setSizePolicy(sizePolicy5)

        self.gridLayout_Isotonic.addWidget(self.lineEdit_IsotonicMaxROM, 3, 3, 1, 1)

        self.label_IsotonicExtensionForce = QLabel(self.Isotonic)
        self.label_IsotonicExtensionForce.setObjectName(u"label_IsotonicExtensionForce")
        sizePolicy3.setHeightForWidth(self.label_IsotonicExtensionForce.sizePolicy().hasHeightForWidth())
        self.label_IsotonicExtensionForce.setSizePolicy(sizePolicy3)

        self.gridLayout_Isotonic.addWidget(self.label_IsotonicExtensionForce, 4, 0, 1, 1)

        self.isotonicRun = QPushButton(self.Isotonic)
        self.isotonicRun.setObjectName(u"isotonicRun")
        self.isotonicRun.setMinimumSize(QSize(100, 0))
        self.isotonicRun.setStyleSheet(u"QPushButton{\n"
"	color: rgb(150, 200, 150);\n"
"	background-color: rgb(0, 120, 0);\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(0,100,0);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"")

        self.gridLayout_Isotonic.addWidget(self.isotonicRun, 5, 2, 1, 2, Qt.AlignHCenter)

        self.gridLayout_Isotonic.setRowStretch(0, 1)
        self.gridLayout_Isotonic.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.Isotonic)
        self.Isokinetic = QWidget()
        self.Isokinetic.setObjectName(u"Isokinetic")
        self.gridLayout_Isokinetic = QGridLayout(self.Isokinetic)
        self.gridLayout_Isokinetic.setObjectName(u"gridLayout_Isokinetic")
        self.gridLayout_Isokinetic.setHorizontalSpacing(50)
        self.gridLayout_Isokinetic.setVerticalSpacing(0)
        self.lineEdit_IsokineticFlexionForce = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticFlexionForce.setObjectName(u"lineEdit_IsokineticFlexionForce")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticFlexionForce, 4, 3, 1, 1)

        self.label_IsokineticExtensionForce = QLabel(self.Isokinetic)
        self.label_IsokineticExtensionForce.setObjectName(u"label_IsokineticExtensionForce")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticExtensionForce, 4, 0, 1, 1)

        self.lineEdit_IsokineticMinROM = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticMinROM.setObjectName(u"lineEdit_IsokineticMinROM")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticMinROM, 3, 1, 1, 1)

        self.lineEdit_IsokineticRepeat = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticRepeat.setObjectName(u"lineEdit_IsokineticRepeat")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticRepeat, 2, 3, 1, 1)

        self.lineEdit_IsokineticSet = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticSet.setObjectName(u"lineEdit_IsokineticSet")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticSet, 2, 1, 1, 1)

        self.label_IsokineticTime = QLabel(self.Isokinetic)
        self.label_IsokineticTime.setObjectName(u"label_IsokineticTime")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticTime, 1, 0, 1, 1)

        self.label_IsokineticRepeat = QLabel(self.Isokinetic)
        self.label_IsokineticRepeat.setObjectName(u"label_IsokineticRepeat")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticRepeat, 2, 2, 1, 1)

        self.label_IsokineticMaxROM = QLabel(self.Isokinetic)
        self.label_IsokineticMaxROM.setObjectName(u"label_IsokineticMaxROM")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticMaxROM, 3, 2, 1, 1)

        self.label_IsokineticExtensionSpeed = QLabel(self.Isokinetic)
        self.label_IsokineticExtensionSpeed.setObjectName(u"label_IsokineticExtensionSpeed")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticExtensionSpeed, 5, 0, 1, 1)

        self.lineEdit_IsokineticExtensionSpeed = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticExtensionSpeed.setObjectName(u"lineEdit_IsokineticExtensionSpeed")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticExtensionSpeed, 5, 1, 1, 1)

        self.label_IsokineticMinROM = QLabel(self.Isokinetic)
        self.label_IsokineticMinROM.setObjectName(u"label_IsokineticMinROM")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticMinROM, 3, 0, 1, 1)

        self.lineEdit_IsokineticRestTime = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticRestTime.setObjectName(u"lineEdit_IsokineticRestTime")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticRestTime, 1, 3, 1, 1)

        self.label_IsokineticRestTime = QLabel(self.Isokinetic)
        self.label_IsokineticRestTime.setObjectName(u"label_IsokineticRestTime")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticRestTime, 1, 2, 1, 1)

        self.label_IsokineticSet = QLabel(self.Isokinetic)
        self.label_IsokineticSet.setObjectName(u"label_IsokineticSet")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticSet, 2, 0, 1, 1)

        self.label_IsokineticFlexionForce = QLabel(self.Isokinetic)
        self.label_IsokineticFlexionForce.setObjectName(u"label_IsokineticFlexionForce")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticFlexionForce, 4, 2, 1, 1)

        self.lineEdit_IsokineticMaxROM = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticMaxROM.setObjectName(u"lineEdit_IsokineticMaxROM")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticMaxROM, 3, 3, 1, 1)

        self.label_Isokinetic = QLabel(self.Isokinetic)
        self.label_Isokinetic.setObjectName(u"label_Isokinetic")
        sizePolicy3.setHeightForWidth(self.label_Isokinetic.sizePolicy().hasHeightForWidth())
        self.label_Isokinetic.setSizePolicy(sizePolicy3)
        self.label_Isokinetic.setStyleSheet(u"font: 30pt \"Segoe UI\";\n"
"color: rgb(170, 85, 255);")

        self.gridLayout_Isokinetic.addWidget(self.label_Isokinetic, 0, 0, 1, 4, Qt.AlignHCenter)

        self.lineEdit_IsokineticFlexionSpeed = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticFlexionSpeed.setObjectName(u"lineEdit_IsokineticFlexionSpeed")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticFlexionSpeed, 5, 3, 1, 1)

        self.lineEdit_IsokineticExtensionForce = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticExtensionForce.setObjectName(u"lineEdit_IsokineticExtensionForce")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticExtensionForce, 4, 1, 1, 1)

        self.lineEdit_IsokineticTime = QLineEdit(self.Isokinetic)
        self.lineEdit_IsokineticTime.setObjectName(u"lineEdit_IsokineticTime")

        self.gridLayout_Isokinetic.addWidget(self.lineEdit_IsokineticTime, 1, 1, 1, 1)

        self.label_IsokineticFlexionSpeed = QLabel(self.Isokinetic)
        self.label_IsokineticFlexionSpeed.setObjectName(u"label_IsokineticFlexionSpeed")

        self.gridLayout_Isokinetic.addWidget(self.label_IsokineticFlexionSpeed, 5, 2, 1, 1)

        self.comboBox_IsokineticEccCon = QComboBox(self.Isokinetic)
        self.comboBox_IsokineticEccCon.addItem("")
        self.comboBox_IsokineticEccCon.addItem("")
        self.comboBox_IsokineticEccCon.addItem("")
        self.comboBox_IsokineticEccCon.addItem("")
        self.comboBox_IsokineticEccCon.setObjectName(u"comboBox_IsokineticEccCon")

        self.gridLayout_Isokinetic.addWidget(self.comboBox_IsokineticEccCon, 6, 0, 1, 2)

        self.isokineticRun = QPushButton(self.Isokinetic)
        self.isokineticRun.setObjectName(u"isokineticRun")
        self.isokineticRun.setMinimumSize(QSize(100, 0))
        self.isokineticRun.setStyleSheet(u"QPushButton{\n"
"	color: rgb(150, 200, 150);\n"
"	background-color: rgb(0, 120, 0);\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(0,100,0);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"")

        self.gridLayout_Isokinetic.addWidget(self.isokineticRun, 6, 2, 1, 2, Qt.AlignHCenter)

        self.gridLayout_Isokinetic.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.Isokinetic)
        self.Spring = QWidget()
        self.Spring.setObjectName(u"Spring")
        self.gridLayout_Spring = QGridLayout(self.Spring)
        self.gridLayout_Spring.setObjectName(u"gridLayout_Spring")
        self.gridLayout_Spring.setHorizontalSpacing(50)
        self.gridLayout_Spring.setVerticalSpacing(0)
        self.lineEdit_SpringMaxROM = QLineEdit(self.Spring)
        self.lineEdit_SpringMaxROM.setObjectName(u"lineEdit_SpringMaxROM")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringMaxROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringMaxROM.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringMaxROM, 3, 3, 1, 1)

        self.label_SpringRestTime = QLabel(self.Spring)
        self.label_SpringRestTime.setObjectName(u"label_SpringRestTime")
        sizePolicy3.setHeightForWidth(self.label_SpringRestTime.sizePolicy().hasHeightForWidth())
        self.label_SpringRestTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringRestTime, 1, 2, 1, 1)

        self.label_SpringSet = QLabel(self.Spring)
        self.label_SpringSet.setObjectName(u"label_SpringSet")
        sizePolicy3.setHeightForWidth(self.label_SpringSet.sizePolicy().hasHeightForWidth())
        self.label_SpringSet.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringSet, 2, 0, 1, 1)

        self.label_SpringInitialPos = QLabel(self.Spring)
        self.label_SpringInitialPos.setObjectName(u"label_SpringInitialPos")
        sizePolicy3.setHeightForWidth(self.label_SpringInitialPos.sizePolicy().hasHeightForWidth())
        self.label_SpringInitialPos.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringInitialPos, 4, 0, 1, 1)

        self.lineEdit_SpringStiffness = QLineEdit(self.Spring)
        self.lineEdit_SpringStiffness.setObjectName(u"lineEdit_SpringStiffness")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringStiffness.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringStiffness, 4, 3, 1, 1)

        self.lineEdit_SpringInitialPos = QLineEdit(self.Spring)
        self.lineEdit_SpringInitialPos.setObjectName(u"lineEdit_SpringInitialPos")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringInitialPos.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringInitialPos.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringInitialPos, 4, 1, 1, 1)

        self.lineEdit_SpringRestTime = QLineEdit(self.Spring)
        self.lineEdit_SpringRestTime.setObjectName(u"lineEdit_SpringRestTime")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringRestTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringRestTime.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringRestTime, 1, 3, 1, 1)

        self.lineEdit_SpringMinROM = QLineEdit(self.Spring)
        self.lineEdit_SpringMinROM.setObjectName(u"lineEdit_SpringMinROM")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringMinROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringMinROM.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringMinROM, 3, 1, 1, 1)

        self.lineEdit_SpringTime = QLineEdit(self.Spring)
        self.lineEdit_SpringTime.setObjectName(u"lineEdit_SpringTime")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringTime.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringTime, 1, 1, 1, 1)

        self.label_SpringRepeat = QLabel(self.Spring)
        self.label_SpringRepeat.setObjectName(u"label_SpringRepeat")
        sizePolicy3.setHeightForWidth(self.label_SpringRepeat.sizePolicy().hasHeightForWidth())
        self.label_SpringRepeat.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringRepeat, 2, 2, 1, 1)

        self.label_SpringTime = QLabel(self.Spring)
        self.label_SpringTime.setObjectName(u"label_SpringTime")
        sizePolicy3.setHeightForWidth(self.label_SpringTime.sizePolicy().hasHeightForWidth())
        self.label_SpringTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringTime, 1, 0, 1, 1)

        self.label_SpringStiffness = QLabel(self.Spring)
        self.label_SpringStiffness.setObjectName(u"label_SpringStiffness")
        sizePolicy3.setHeightForWidth(self.label_SpringStiffness.sizePolicy().hasHeightForWidth())
        self.label_SpringStiffness.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringStiffness, 4, 2, 1, 1)

        self.lineEdit_SpringSet = QLineEdit(self.Spring)
        self.lineEdit_SpringSet.setObjectName(u"lineEdit_SpringSet")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringSet.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringSet.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringSet, 2, 1, 1, 1)

        self.label_SpringMaxROM = QLabel(self.Spring)
        self.label_SpringMaxROM.setObjectName(u"label_SpringMaxROM")
        sizePolicy3.setHeightForWidth(self.label_SpringMaxROM.sizePolicy().hasHeightForWidth())
        self.label_SpringMaxROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringMaxROM, 3, 2, 1, 1)

        self.label_SpringMinROM = QLabel(self.Spring)
        self.label_SpringMinROM.setObjectName(u"label_SpringMinROM")
        sizePolicy3.setHeightForWidth(self.label_SpringMinROM.sizePolicy().hasHeightForWidth())
        self.label_SpringMinROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Spring.addWidget(self.label_SpringMinROM, 3, 0, 1, 1)

        self.label_Spring = QLabel(self.Spring)
        self.label_Spring.setObjectName(u"label_Spring")
        sizePolicy3.setHeightForWidth(self.label_Spring.sizePolicy().hasHeightForWidth())
        self.label_Spring.setSizePolicy(sizePolicy3)
        self.label_Spring.setStyleSheet(u"font: 30pt \"Segoe UI\";\n"
"color: rgb(170, 85, 255);")

        self.gridLayout_Spring.addWidget(self.label_Spring, 0, 0, 1, 4, Qt.AlignHCenter)

        self.lineEdit_SpringRepeat = QLineEdit(self.Spring)
        self.lineEdit_SpringRepeat.setObjectName(u"lineEdit_SpringRepeat")
        sizePolicy5.setHeightForWidth(self.lineEdit_SpringRepeat.sizePolicy().hasHeightForWidth())
        self.lineEdit_SpringRepeat.setSizePolicy(sizePolicy5)

        self.gridLayout_Spring.addWidget(self.lineEdit_SpringRepeat, 2, 3, 1, 1)

        self.springRun = QPushButton(self.Spring)
        self.springRun.setObjectName(u"springRun")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.springRun.sizePolicy().hasHeightForWidth())
        self.springRun.setSizePolicy(sizePolicy6)
        self.springRun.setMinimumSize(QSize(100, 0))
        self.springRun.setStyleSheet(u"QPushButton{\n"
"	color: rgb(150, 200, 150);\n"
"	background-color: rgb(0, 120, 0);\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(0,100,0);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"")

        self.gridLayout_Spring.addWidget(self.springRun, 5, 2, 1, 2, Qt.AlignHCenter)

        self.gridLayout_Spring.setColumnStretch(0, 1)
        self.gridLayout_Spring.setColumnStretch(1, 2)
        self.gridLayout_Spring.setColumnStretch(2, 1)
        self.gridLayout_Spring.setColumnStretch(3, 2)
        self.stackedWidget.addWidget(self.Spring)
        self.Water = QWidget()
        self.Water.setObjectName(u"Water")
        self.gridLayout_Water = QGridLayout(self.Water)
        self.gridLayout_Water.setObjectName(u"gridLayout_Water")
        self.gridLayout_Water.setHorizontalSpacing(50)
        self.gridLayout_Water.setVerticalSpacing(0)
        self.label_WaterTime = QLabel(self.Water)
        self.label_WaterTime.setObjectName(u"label_WaterTime")
        sizePolicy3.setHeightForWidth(self.label_WaterTime.sizePolicy().hasHeightForWidth())
        self.label_WaterTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.label_WaterTime, 1, 0, 1, 1)

        self.lineEdit_WaterTime = QLineEdit(self.Water)
        self.lineEdit_WaterTime.setObjectName(u"lineEdit_WaterTime")
        sizePolicy3.setHeightForWidth(self.lineEdit_WaterTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_WaterTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.lineEdit_WaterTime, 1, 1, 1, 1)

        self.label_WaterRestTime = QLabel(self.Water)
        self.label_WaterRestTime.setObjectName(u"label_WaterRestTime")
        sizePolicy3.setHeightForWidth(self.label_WaterRestTime.sizePolicy().hasHeightForWidth())
        self.label_WaterRestTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.label_WaterRestTime, 1, 2, 1, 1)

        self.lineEdit_WaterRestTime = QLineEdit(self.Water)
        self.lineEdit_WaterRestTime.setObjectName(u"lineEdit_WaterRestTime")
        sizePolicy3.setHeightForWidth(self.lineEdit_WaterRestTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_WaterRestTime.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.lineEdit_WaterRestTime, 1, 3, 1, 1)

        self.label_WaterSet = QLabel(self.Water)
        self.label_WaterSet.setObjectName(u"label_WaterSet")
        sizePolicy3.setHeightForWidth(self.label_WaterSet.sizePolicy().hasHeightForWidth())
        self.label_WaterSet.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.label_WaterSet, 2, 0, 1, 1)

        self.lineEdit_WaterSet = QLineEdit(self.Water)
        self.lineEdit_WaterSet.setObjectName(u"lineEdit_WaterSet")
        sizePolicy3.setHeightForWidth(self.lineEdit_WaterSet.sizePolicy().hasHeightForWidth())
        self.lineEdit_WaterSet.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.lineEdit_WaterSet, 2, 1, 1, 1)

        self.label_WaterRepeat = QLabel(self.Water)
        self.label_WaterRepeat.setObjectName(u"label_WaterRepeat")
        sizePolicy3.setHeightForWidth(self.label_WaterRepeat.sizePolicy().hasHeightForWidth())
        self.label_WaterRepeat.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.label_WaterRepeat, 2, 2, 1, 1)

        self.lineEdit_WaterRepeat = QLineEdit(self.Water)
        self.lineEdit_WaterRepeat.setObjectName(u"lineEdit_WaterRepeat")
        sizePolicy3.setHeightForWidth(self.lineEdit_WaterRepeat.sizePolicy().hasHeightForWidth())
        self.lineEdit_WaterRepeat.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.lineEdit_WaterRepeat, 2, 3, 1, 1)

        self.label_WaterMinROM = QLabel(self.Water)
        self.label_WaterMinROM.setObjectName(u"label_WaterMinROM")
        sizePolicy3.setHeightForWidth(self.label_WaterMinROM.sizePolicy().hasHeightForWidth())
        self.label_WaterMinROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.label_WaterMinROM, 3, 0, 1, 1)

        self.lineEdit_WaterMinROM = QLineEdit(self.Water)
        self.lineEdit_WaterMinROM.setObjectName(u"lineEdit_WaterMinROM")
        sizePolicy3.setHeightForWidth(self.lineEdit_WaterMinROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_WaterMinROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.lineEdit_WaterMinROM, 3, 1, 1, 1)

        self.label_WaterMaxROM = QLabel(self.Water)
        self.label_WaterMaxROM.setObjectName(u"label_WaterMaxROM")
        sizePolicy3.setHeightForWidth(self.label_WaterMaxROM.sizePolicy().hasHeightForWidth())
        self.label_WaterMaxROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.label_WaterMaxROM, 3, 2, 1, 1)

        self.lineEdit_WaterMaxROM = QLineEdit(self.Water)
        self.lineEdit_WaterMaxROM.setObjectName(u"lineEdit_WaterMaxROM")
        sizePolicy3.setHeightForWidth(self.lineEdit_WaterMaxROM.sizePolicy().hasHeightForWidth())
        self.lineEdit_WaterMaxROM.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.lineEdit_WaterMaxROM, 3, 3, 1, 1)

        self.label_WaterDensity = QLabel(self.Water)
        self.label_WaterDensity.setObjectName(u"label_WaterDensity")
        sizePolicy3.setHeightForWidth(self.label_WaterDensity.sizePolicy().hasHeightForWidth())
        self.label_WaterDensity.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.label_WaterDensity, 4, 0, 1, 1)

        self.lineEdit_WaterDensity = QLineEdit(self.Water)
        self.lineEdit_WaterDensity.setObjectName(u"lineEdit_WaterDensity")
        sizePolicy3.setHeightForWidth(self.lineEdit_WaterDensity.sizePolicy().hasHeightForWidth())
        self.lineEdit_WaterDensity.setSizePolicy(sizePolicy3)

        self.gridLayout_Water.addWidget(self.lineEdit_WaterDensity, 4, 1, 1, 1)

        self.label_Water = QLabel(self.Water)
        self.label_Water.setObjectName(u"label_Water")
        sizePolicy3.setHeightForWidth(self.label_Water.sizePolicy().hasHeightForWidth())
        self.label_Water.setSizePolicy(sizePolicy3)
        self.label_Water.setFont(font4)
        self.label_Water.setStyleSheet(u"font: 30pt \"Segoe UI\";\n"
"color: rgb(170, 85, 255);")

        self.gridLayout_Water.addWidget(self.label_Water, 0, 0, 1, 4, Qt.AlignHCenter)

        self.waterRun = QPushButton(self.Water)
        self.waterRun.setObjectName(u"waterRun")
        self.waterRun.setMinimumSize(QSize(100, 0))
        self.waterRun.setStyleSheet(u"QPushButton{\n"
"	color: rgb(150, 200, 150);\n"
"	background-color: rgb(0, 120, 0);\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(0,100,0);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(0,50,0);\n"
"}\n"
"")

        self.gridLayout_Water.addWidget(self.waterRun, 4, 2, 1, 2, Qt.AlignHCenter)

        self.gridLayout_Water.setColumnStretch(0, 1)
        self.gridLayout_Water.setColumnStretch(1, 2)
        self.gridLayout_Water.setColumnStretch(2, 1)
        self.gridLayout_Water.setColumnStretch(3, 2)
        self.stackedWidget.addWidget(self.Water)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 278, 222))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy7)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Homing.setText(QCoreApplication.translate("MainWindow", u"Homing", None))
        self.btn_Passive.setText(QCoreApplication.translate("MainWindow", u"Passive", None))
        self.btn_Isometric.setText(QCoreApplication.translate("MainWindow", u"Isometric", None))
        self.btn_Isotonic.setText(QCoreApplication.translate("MainWindow", u"Isotonic", None))
        self.btn_Isokinetic.setText(QCoreApplication.translate("MainWindow", u"Isokinetic", None))
        self.btn_Spring.setText(QCoreApplication.translate("MainWindow", u"Spring Form", None))
        self.btn_Water.setText(QCoreApplication.translate("MainWindow", u"Water Form", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"FUM - Physio", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.homingRun.setText(QCoreApplication.translate("MainWindow", u"Homing", None))
        self.text_Homing.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:5px;\"><span style=\" font-size:12pt;\">Press the button to start homing...</span></p></body></html>", None))
        self.label_PassiveSet.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.label_PassiveSpeed.setText(QCoreApplication.translate("MainWindow", u"Speed: (deg/s)", None))
        self.label_PassiveRestTime.setText(QCoreApplication.translate("MainWindow", u"Rest Time: (s)", None))
        self.label_PassiveMinROM.setText(QCoreApplication.translate("MainWindow", u"Min ROM:", None))
        self.label_PassiveMaxROM.setText(QCoreApplication.translate("MainWindow", u"Max ROM:", None))
        self.label_PassiveTime.setText(QCoreApplication.translate("MainWindow", u"Time: (s)", None))
        self.label_PassiveRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat:", None))
        self.label_Passive.setText(QCoreApplication.translate("MainWindow", u"Passive", None))
        self.passiveRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_IsometricTime.setText(QCoreApplication.translate("MainWindow", u"Time: (s)", None))
        self.groupBox_IsometricPos.setTitle(QCoreApplication.translate("MainWindow", u"Positions (deg)", None))
        self.label_IsometricPos1.setText(QCoreApplication.translate("MainWindow", u"Position 1:", None))
        self.label_IsometricPos2.setText(QCoreApplication.translate("MainWindow", u"Position 2:", None))
        self.label_IsometricPos3.setText(QCoreApplication.translate("MainWindow", u"Position 3:", None))
        self.label_IsometricSet.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.label_IsometricRestTime.setText(QCoreApplication.translate("MainWindow", u"Rest Time: (s)", None))
        self.IsometricRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_IsometricRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat:", None))
        self.label_IsometricForce.setText(QCoreApplication.translate("MainWindow", u"Force: (N)", None))
        self.label_IsometricHoldTime.setText(QCoreApplication.translate("MainWindow", u"Hold TIme: (s)", None))
        self.label_Isometric.setText(QCoreApplication.translate("MainWindow", u"Isometric", None))
        self.label_IsotonicFlexionForce.setText(QCoreApplication.translate("MainWindow", u"Flexion Force: (N)", None))
        self.label_IsotonicTime.setText(QCoreApplication.translate("MainWindow", u"Time: (s)", None))
        self.label_IsotonicMaxROM.setText(QCoreApplication.translate("MainWindow", u"Max ROM:", None))
        self.label_IsotonicRestTime.setText(QCoreApplication.translate("MainWindow", u"Rest Time: (s)", None))
        self.label_Isotonic.setText(QCoreApplication.translate("MainWindow", u"Isotonic", None))
        self.label_IsotonicSet.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.label_IsotonicMinROM.setText(QCoreApplication.translate("MainWindow", u"Min ROM:", None))
        self.label_IsotonicRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat:", None))
        self.label_IsotonicExtensionForce.setText(QCoreApplication.translate("MainWindow", u"Extension Force: (N)", None))
        self.isotonicRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_IsokineticExtensionForce.setText(QCoreApplication.translate("MainWindow", u"Extension Force: (N)", None))
        self.label_IsokineticTime.setText(QCoreApplication.translate("MainWindow", u"Time: (s)", None))
        self.label_IsokineticRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat:", None))
        self.label_IsokineticMaxROM.setText(QCoreApplication.translate("MainWindow", u"Max ROM:", None))
        self.label_IsokineticExtensionSpeed.setText(QCoreApplication.translate("MainWindow", u"Extension Speed: (deg/s)", None))
        self.label_IsokineticMinROM.setText(QCoreApplication.translate("MainWindow", u"Min ROM:", None))
        self.label_IsokineticRestTime.setText(QCoreApplication.translate("MainWindow", u"Rest Time: (s)", None))
        self.label_IsokineticSet.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.label_IsokineticFlexionForce.setText(QCoreApplication.translate("MainWindow", u"Flexion Force: (N)", None))
        self.label_Isokinetic.setText(QCoreApplication.translate("MainWindow", u"Isokinetic", None))
        self.label_IsokineticFlexionSpeed.setText(QCoreApplication.translate("MainWindow", u"Flexion Speed: (deg/s)", None))
        self.comboBox_IsokineticEccCon.setItemText(0, QCoreApplication.translate("MainWindow", u"ECC/CON", None))
        self.comboBox_IsokineticEccCon.setItemText(1, QCoreApplication.translate("MainWindow", u"ECC/ECC", None))
        self.comboBox_IsokineticEccCon.setItemText(2, QCoreApplication.translate("MainWindow", u"CON/CON", None))
        self.comboBox_IsokineticEccCon.setItemText(3, QCoreApplication.translate("MainWindow", u"CON/ECC", None))

        self.isokineticRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_SpringRestTime.setText(QCoreApplication.translate("MainWindow", u"Rest Time: (s)", None))
        self.label_SpringSet.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.label_SpringInitialPos.setText(QCoreApplication.translate("MainWindow", u"Initial Position: (deg)", None))
        self.label_SpringRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat:", None))
        self.label_SpringTime.setText(QCoreApplication.translate("MainWindow", u"Time: (s)", None))
        self.label_SpringStiffness.setText(QCoreApplication.translate("MainWindow", u"Stiffness:", None))
        self.label_SpringMaxROM.setText(QCoreApplication.translate("MainWindow", u"Max ROM:", None))
        self.label_SpringMinROM.setText(QCoreApplication.translate("MainWindow", u"Min ROM:", None))
        self.label_Spring.setText(QCoreApplication.translate("MainWindow", u"Spring Form", None))
        self.springRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_WaterTime.setText(QCoreApplication.translate("MainWindow", u"Time: (s)", None))
        self.label_WaterRestTime.setText(QCoreApplication.translate("MainWindow", u"Rest Time: (s)", None))
        self.label_WaterSet.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.label_WaterRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat:", None))
        self.label_WaterMinROM.setText(QCoreApplication.translate("MainWindow", u"Min ROM:", None))
        self.label_WaterMaxROM.setText(QCoreApplication.translate("MainWindow", u"Max ROM:", None))
        self.label_WaterDensity.setText(QCoreApplication.translate("MainWindow", u"Density:", None))
        self.label_Water.setText(QCoreApplication.translate("MainWindow", u"Water Form", None))
        self.waterRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: M. J. Javanbakht", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

