__author__ = 'Maxiee'
from PyQt4 import QtCore, QtGui


class HomePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)

        self.clock = QtGui.QLCDNumber()
        self.clock.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.clock.setMinimumHeight(50)
        self.clock.setSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Fixed)

        self.date = QtGui.QLabel()
        self.date.setText(
            QtCore.QDateTime.currentDateTime()
            .toString("yyyy年MM月dd日 dddd"))
        self.date.setAlignment(QtCore.Qt.AlignRight)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # Weather
        from widgets.homepage import weatherapi
        weatherGrid = QtGui.QGridLayout()
        weatherGrid.setMargin(1)
        (ok, date, minTemp, maxTemp, weather) = weatherapi.getWeather7Days()
        for i in range(5):
            weatherVBox = QtGui.QVBoxLayout()
            weatherVBox.addWidget(QtGui.QLabel(date[i] if ok else ""))
            weatherVBox.addWidget(QtGui.QLabel(str(minTemp[i])+"℃" if ok else ""[i]))
            weatherVBox.addWidget(QtGui.QLabel(str(maxTemp[i])+"℃" if ok else "暂时无网络"[i]))
            weatherVBox.addWidget(QtGui.QLabel(weather[i]) if ok else "检查后刷新"[i])
            weatherGrid.addLayout(weatherVBox, 0, i)

        # Daily function
        dailyGrid = QtGui.QGridLayout()
        # ConnectNetwork
        networkButton = QtGui.QPushButton()
        networkButton.setText("校园网")
        from widgets.homepage import networkutils
        networkButton.clicked.connect(networkutils.connectNetwork)
        dailyGrid.addWidget(networkButton, 0, 0)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.clock)
        mainLayout.addWidget(self.date)
        mainLayout.addLayout(weatherGrid)
        mainLayout.addStretch(1)
        mainLayout.addLayout(dailyGrid)

        self.setLayout(mainLayout)
        self.setWindowTitle("主页")

    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("hh:mm")
        if(time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.clock.display(text)
