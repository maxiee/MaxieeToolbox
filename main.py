__author__ = 'Maxiee'
from PyQt4 import QtCore, QtGui
import widgets.homepage.homepage
import os


class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.myIcon = QtGui.QIcon(os.path.join(".", "MyData", "icon.jpg"))
        self.icon = QtGui.QSystemTrayIcon()
        self.icon.setIcon(self.myIcon)
        self.icon.activated.connect(self.taryActivied)
        self.icon.show()
        self.setWindowIcon(self.myIcon)

        self.homepage = widgets.homepage.homepage.HomePage()

        self.mainStack = QtGui.QStackedWidget()
        self.mainStack.addWidget(self.homepage)

        self.mainPageComboBox = QtGui.QComboBox()
        self.mainPageComboBox.addItem("主页")

        QtCore.QObject.connect(
            self.mainPageComboBox,
            QtCore.SIGNAL('activated(int)'),
            self.mainStack,
            QtCore.SLOT('setCurrentIndex(int)'))

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.mainPageComboBox)
        mainLayout.addWidget(self.mainStack)

        self.setGeometry(100,100,300,600)
        self.setLayout(mainLayout)
        self.setWindowTitle("Maxiee工具箱")

    def closeEvent(self, QCloseEvent):
        reply = QtGui.QMessageBox.question(
            self,  'Quit', 'Are you sure to quit?',
            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            self.icon.show()
            self.hide()
            QCloseEvent.ignore()

    def taryActivied(self, reason):
        if reason == 2:
            self.show()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())