__author__ = 'Maxiee'
from PyQt4 import QtCore, QtGui
import widgets.homepage.homepage

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

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

        self.setLayout(mainLayout)
        self.setWindowTitle("Maxiee工具箱")

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())