from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow
from ui_file.login_UI import Ui_MainWindow
from PyQt5.QtGui import QMovie
import static.resources_rc
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._startPos = None
        self._endPos = None
        self._tracking = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.loginButton.clicked.connect(self.loginBtn_clicked)
        self.movie = QMovie(":/image/image/original.gif")
        self.ui.label.setMovie(self.movie)
        self.startAnimation()


    def loginBtn_clicked(self):
        """
        Function for handling login button click.
        """
        username = self.ui.lineUser.text().strip()
        password = self.ui.linePsw.text().strip()

        # Check the password
        if password == "0" and username == "admin":
            self.ui.label_5.setVisible(False)
            QMessageBox.warning(self, "Error", "Correct password!")
        else:
            self.ui.label_5.setVisible(True)

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
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
