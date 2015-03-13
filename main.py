__author__ = 'Maxiee'
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.HelloLabel = QtGui.QLabel("Hello!")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.HelloLabel)

        self.setLayout(mainLayout)
        self.setWindowTitle("Maxiee工具箱")

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())