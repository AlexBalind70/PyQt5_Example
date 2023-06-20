# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 572)
        MainWindow.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 85, 127);\n"
"\n"
"    border:none;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.199, y1:0.244318, x2:1, y2:1, stop:0 rgba(66, 2, 157), stop:1 rgba(rgb(4,7,47)));\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.widget_4 = QtWidgets.QWidget()
        self.widget_4.setObjectName("widget_4")
        self.stackedWidget.addWidget(self.widget_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 350))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widget_2.setStyleSheet("background-color: transparent;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(60, 60))
        self.label_3.setMaximumSize(QtCore.QSize(200, 270))
        self.label_3.setStyleSheet("background-color: transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/image/images/night.gif"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 3, 1)
        self.currentTempLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(60)
        self.currentTempLabel.setFont(font)
        self.currentTempLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.currentTempLabel.setStyleSheet("background-color: transparent;")
        self.currentTempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTempLabel.setObjectName("currentTempLabel")
        self.gridLayout_3.addWidget(self.currentTempLabel, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.skyLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.skyLabel.setFont(font)
        self.skyLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.skyLabel.setStyleSheet("background-color: transparent;")
        self.skyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.skyLabel.setObjectName("skyLabel")
        self.gridLayout_3.addWidget(self.skyLabel, 2, 0, 1, 1, QtCore.Qt.AlignTop)
        self.tempLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tempLabel.setFont(font)
        self.tempLabel.setStyleSheet("background-color: transparent;")
        self.tempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.gridLayout_3.addWidget(self.tempLabel, 6, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.cityLabel = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cityLabel.setFont(font)
        self.cityLabel.setMouseTracking(False)
        self.cityLabel.setFocusPolicy(QtCore.Qt.TabFocus)
        self.cityLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.cityLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cityLabel.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/map-pin (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cityLabel.setIcon(icon)
        self.cityLabel.setIconSize(QtCore.QSize(16, 16))
        self.cityLabel.setAutoRepeat(False)
        self.cityLabel.setObjectName("cityLabel")
        self.gridLayout_3.addWidget(self.cityLabel, 3, 0, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout_3.addWidget(self.timeLabel, 6, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.dateLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout_3.addWidget(self.dateLabel, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setStyleSheet("background-color: transparent;\n"
"font: 75 8pt \"Arial\";")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 6)
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cloudsLabel = QtWidgets.QLabel(self.widget_3)
        self.cloudsLabel.setObjectName("cloudsLabel")
        self.gridLayout_5.addWidget(self.cloudsLabel, 1, 2, 1, 1, QtCore.Qt.AlignTop)
        self.pressureLabel = QtWidgets.QLabel(self.widget_3)
        self.pressureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pressureLabel.setObjectName("pressureLabel")
        self.gridLayout_5.addWidget(self.pressureLabel, 1, 5, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/icons/icons/140-1405202_windy-weather-icon-wind-weather-symbols-clipart 1.svg"))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/icons/icons/cloud.svg"))
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/icons/icons/Group.svg"))
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 1, 4, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.humidityLabel = QtWidgets.QLabel(self.widget_3)
        self.humidityLabel.setObjectName("humidityLabel")
        self.gridLayout_5.addWidget(self.humidityLabel, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMaximumSize(QtCore.QSize(24, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/droplet.svg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 4, 1, 1)
        self.speedLabel = QtWidgets.QLabel(self.widget_3)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout_5.addWidget(self.speedLabel, 0, 2, 1, 2)
        self.gridLayout_4.addWidget(self.widget_3, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(40, 60))
        self.widget.setStyleSheet("background-color: transparent;")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.citySearch = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.citySearch.setFont(font)
        self.citySearch.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.citySearch.setInputMask("")
        self.citySearch.setAlignment(QtCore.Qt.AlignCenter)
        self.citySearch.setObjectName("citySearch")
        self.gridLayout_2.addWidget(self.citySearch, 2, 1, 1, 3)
        self.rollUpButton = QtWidgets.QPushButton(self.widget)
        self.rollUpButton.setMaximumSize(QtCore.QSize(24, 24))
        self.rollUpButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rollUpButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rollUpButton.setIcon(icon1)
        self.rollUpButton.setIconSize(QtCore.QSize(24, 24))
        self.rollUpButton.setObjectName("rollUpButton")
        self.gridLayout_2.addWidget(self.rollUpButton, 0, 8, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon2)
        self.searchButton.setIconSize(QtCore.QSize(20, 20))
        self.searchButton.setAutoRepeat(False)
        self.searchButton.setAutoExclusive(False)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 2, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 2, 1)
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setMaximumSize(QtCore.QSize(24, 24))
        self.closeButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.setAutoDefault(False)
        self.closeButton.setDefault(False)
        self.closeButton.setFlat(False)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 0, 9, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/images/raccoon.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.currentTempLabel.setText(_translate("MainWindow", "   19 °"))
        self.skyLabel.setText(_translate("MainWindow", "Clear"))
        self.tempLabel.setText(_translate("MainWindow", "19° / 7° Feels like 14°"))
        self.cityLabel.setText(_translate("MainWindow", "Tomsk"))
        self.timeLabel.setText(_translate("MainWindow", "3:43"))
        self.dateLabel.setText(_translate("MainWindow", "17 Jun 2023"))
        self.cloudsLabel.setText(_translate("MainWindow", "Clouds 87%"))
        self.pressureLabel.setText(_translate("MainWindow", "Pressure 1017hPa"))
        self.humidityLabel.setText(_translate("MainWindow", "Humidity 50%"))
        self.speedLabel.setText(_translate("MainWindow", "Speed of wind 3.16m/s"))
        self.citySearch.setText(_translate("MainWindow", "Search city"))
import static.resources_rc
