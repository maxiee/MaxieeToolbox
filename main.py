__author__ = 'Maxiee'
from PyQt4 import QtCore, QtGui
import widgets.homepage.homepage
import widgets.weibo.weibo
import os


class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.myIcon = QtGui.QIcon(os.path.join(".", "MyData", "icon.jpg"))
        menu = QtGui.QMenu()
        exitAction = menu.addAction("Exit")
        self.connect(exitAction,QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("close()"))
        self.icon = QtGui.QSystemTrayIcon()
        self.icon.setIcon(self.myIcon)
        self.icon.activated.connect(self.taryActivied)
        self.icon.setContextMenu(menu)
        self.icon.show()
        self.icon.showMessage("欢迎！", "Have a good day!")
        self.setWindowIcon(self.myIcon)

        self.homepage = widgets.homepage.homepage.HomePage()
        self.weibo = widgets.weibo.weibo.Weibo()

        self.mainStack = QtGui.QStackedWidget()
        self.mainStack.addWidget(self.homepage)
        self.mainStack.addWidget(self.weibo)

        self.mainPageComboBox = QtGui.QComboBox()
        self.mainPageComboBox.addItem("主页")
        self.mainPageComboBox.addItem("微博")

        QtCore.QObject.connect(
            self.mainPageComboBox,
            QtCore.SIGNAL('activated(int)'),
            self.mainStack,
            QtCore.SLOT('setCurrentIndex(int)'))

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.mainPageComboBox)
        mainLayout.addWidget(self.mainStack)

        self.setGeometry(100,100,300,600)
        self.setMaximumWidth(600)
        self.setLayout(mainLayout)
        self.setWindowTitle("Maxiee工具箱")

    def taryActivied(self, reason):
        # 3-单击 2-双击 1-右键单击
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.show()
        else:
            self.hide()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())