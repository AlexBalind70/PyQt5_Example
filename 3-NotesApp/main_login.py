from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QPushButton

from ui_file.login_ui import Ui_LoginWindow
from main_page import MainPageWindow
import static.resources_rc
import sys


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.main_window = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self._startPos = None
        self._endPos = None
        self._tracking = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        self.movie = QMovie(":/image/images/racoon.gif")
        self.ui.label.setMovie(self.movie)
        self.startAnimation()
        self.ui.message_Label.setVisible(False)
        self.ui.sign_up_Buttom.clicked.connect(self.sign_up_Buttom_clicked)
        self.ui.closeButton.clicked.connect(qApp.quit)

    def sign_up_Buttom_clicked(self):
        """
        function for login app
        """
        username = self.ui.user_Line.text().strip()
        password = self.ui.password_Line.text().strip()

        # Check the password
        if password == "0" and username == "admin":
            # Create a new instance of the main window
            self.main_window = MainPageWindow()
            # Show the new window
            self.main_window.show()
            # Close the login window
            self.close()
        else:
            # Show an error message
            self.ui.message_Label.setVisible(True)

    def on_vision_pass_Buttom_clicked(self):
        self.ui.password_Line.setEchoMode(QtWidgets.QLineEdit.Normal)
        QTimer.singleShot(500, lambda: self.ui.password_Line.setEchoMode(QtWidgets.QLineEdit.Password))

    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.create_account_Button.findChildren(QPushButton)

        for btn in btn_list:
            if index in [0, 1]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_create_account_Button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_back_Button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
