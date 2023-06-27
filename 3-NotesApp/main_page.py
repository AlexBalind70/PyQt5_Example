from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QPushButton

from ui_file.main_page_ui import Ui_MainPageWindow
from main_add_note import NoteWindow


class MainPageWindow(QMainWindow):
    def __init__(self):
        super(MainPageWindow, self).__init__()
        self.note_window = None
        self.ui_page = Ui_MainPageWindow()
        self.ui_page.setupUi(self)

        self._startPos = None
        self._endPos = None
        self._tracking = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_page.main_Menu.hide()
        self.ui_page.pushButton_12.clicked.connect(lambda: self.setWindowState(self.windowState() | Qt.WindowMinimized))
        self.ui_page.pushButton_11.clicked.connect(qApp.quit)

    def on_button_add_note_clicked(self):
        self.note_window = NoteWindow()
        # Show the new window
        self.note_window.show()
        
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui_page.buttonMenu.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_button_left_Home_toggled(self):
        self.ui_page.stackedWidget.setCurrentIndex(0)

    def on_button_leftCalendar_toggled(self):
        self.ui_page.stackedWidget.setCurrentIndex(1)

    def on_button_left_Notes_toggled(self):
        self.ui_page.stackedWidget.setCurrentIndex(2)

    def on_button_left_Settings_toggled(self):
        self.ui_page.stackedWidget.setCurrentIndex(3)



    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self._tracking:
            self._endPos = a0.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

