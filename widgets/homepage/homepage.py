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

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.clock)
        mainLayout.addWidget(self.date)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)
        self.setWindowTitle("主页")

    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("hh:mm")
        if(time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.clock.display(text)