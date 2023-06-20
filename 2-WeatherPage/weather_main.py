import sys
import datetime
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from ui_file.weather_ui import *


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

        self.ui.searchButton.clicked.connect(self.request_weather)
        self.ui.rollUpButton.clicked.connect(lambda: self.setWindowState(self.windowState() | Qt.WindowMinimized))
        self.ui.closeButton.clicked.connect(qApp.quit)

        self.night = "background-color: qlineargradient(spread:pad, x1:0.199, y1:0.244318, x2:1, y2:1, stop:0 rgba(" \
                     "66, 2, ""157), stop:1 rgba(rgb(4,7,47)));\n"\
                     "\n""color: rgb(255, 255, 255);\n"""
        self.lineEdit_clear_sky = "color: rgb(85, 170, 255);\n" \
                                  "background-color: rgb(255, 255, 255);"
        self.lineEdit_cloud = "color: rgb(0, 0, 0);\n" \
                              "background-color: rgb(255, 255, 255);"
        self.lineEdit_night = "color: rgb(85, 85, 255);\n"\
                              "background-color: rgb(255, 255, 255);"
        self.clear_sky = "background-color: qlineargradient(spread:pad, x1:0.199, y1:0.244318, x2:1, y2:1," \
                         "stop:0 rgba(49,""209,248), \
                         stop:1 rgba(22,144,231));\n"\
                         'color: rgb(255, 255, 255);\n'
        self.overcast_cloud = "background-color: qlineargradient(spread:pad, x1:0.199, y1:0.244318, x2:1, y2:1,"\
                              "stop:0 rgba(188,194,198), stop:1 rgba(45,63,81));\n"\
                              "\n""color: rgb(255, 255, 255);\n"""

        self.sunny_gif = ":/image/images/sun1.gif"
        self.cloud_gif = ":/image/images/cloud.gif"
        self.rain_gif = ":/image/images/rain.gif"
        self.night_gif = ":/image/images/night.gif"

    def request_weather(self):
        city = self.ui.citySearch.text()

        if city:
            city = city.capitalize()
            api_key = "79d1ca96933b0328e1c7e3e7a26cb347"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                self.temperature = round(data["main"]["temp"])
                self.pressure = data['main']['pressure']
                self.humidity = data["main"]["humidity"]
                self.min_temp = round(data["main"]["temp_min"])
                self.max_temp = round(data["main"]["temp_max"])
                self.feels_temp = round(data["main"]["feels_like"])
                self.description = data["weather"][0]["description"]
                self.wind_speed = data["wind"]["speed"]
                self.timezone_offset = data['timezone']
                self.cloud = data["clouds"]["all"]
                self.city = city
                self.data = data
                self.result_weather()
                self.get_local_time()
                self.theme_weather_app()

    def result_weather(self):
        self.ui.cityLabel.setText(f"{self.city}")
        self.ui.currentTempLabel.setText(f"{self.temperature}°")
        self.ui.humidityLabel.setText(f"Humidity: {self.humidity}%")
        self.ui.pressureLabel.setText(f"Pressure: {self.pressure} hPa")
        self.ui.speedLabel.setText(f"Wind Speed: {self.wind_speed} m/s")
        self.ui.cloudsLabel.setText(f"Clouds {self.cloud}%")
        self.ui.tempLabel.setText(f"{self.max_temp}° / {self.min_temp}° Feels like {self.feels_temp}°")

        if "rain" in self.description.capitalize():
            self.ui.skyLabel.setText("Rain")
        else:
            self.ui.skyLabel.setText(f"{self.description.capitalize()}")

    def get_local_time(self):
        self.local_time = datetime.datetime.utcfromtimestamp(self.data['dt']) + datetime.timedelta(
            seconds=self.timezone_offset)
        self.local_time_formatted = self.local_time.strftime("%H:%M")
        self.ui.timeLabel.setText(self.local_time_formatted)
        self.ui.dateLabel.setText(self.local_time.strftime("%b %d"))

    def theme_time(self):

        start_time = datetime.time(7, 1)
        end_time = datetime.time(20, 59)

        if start_time <= self.local_time.time() <= end_time:
            print(1)

        else:
            if self.description.capitalize() == "Clear sky":
                self.gif_animation(self.night_gif)
            self.ui.centralwidget.setStyleSheet(self.night)

    def gif_animation(self, name_gif):
        self.movie = QMovie(name_gif)
        self.ui.label_3.setMovie(self.movie)
        self.startAnimation()

    def theme_weather_app(self):

        if self.description.capitalize() == "Clear sky":
            self.gif_animation(self.sunny_gif)
            self.ui.centralwidget.setStyleSheet(self.clear_sky)
            self.ui.citySearch.setStyleSheet(self.lineEdit_clear_sky)

        elif "clouds" in self.description.capitalize():
            self.gif_animation(self.cloud_gif)

            if self.description.capitalize() == "Broken clouds" or "Scattered clouds ":
                self.ui.centralwidget.setStyleSheet(self.clear_sky)
                self.ui.citySearch.setStyleSheet(self.lineEdit_clear_sky)
            if self.description.capitalize() == "Overcast clouds":
                self.ui.citySearch.setStyleSheet(self.lineEdit_cloud)
                self.ui.centralwidget.setStyleSheet(self.overcast_cloud)

        elif "rain" in self.description.capitalize():
            self.gif_animation(self.rain_gif)
            self.ui.label_3.setScaledContents(True)
            self.ui.centralwidget.setStyleSheet(self.overcast_cloud)
            self.ui.citySearch.setStyleSheet(self.lineEdit_cloud)

        else:
            self.ui.centralwidget.setStyleSheet(self.clear_sky)

        self.theme_time()

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
