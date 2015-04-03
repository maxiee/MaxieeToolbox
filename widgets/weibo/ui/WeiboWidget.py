__author__ = 'Maxiee'
from PyQt4 import QtGui


class WeiboWidget(QtGui.QWidget):
    def __init__(self, parent=None, user="", text="", reUser=None, reText=None):
        super(WeiboWidget, self).__init__(parent)
        mainLayout = QtGui.QVBoxLayout()
        weiboLabel = QtGui.QLabel(user + ":" + text)
        weiboLabel.setWordWrap(True)
        mainLayout.addWidget(weiboLabel)
        if reUser is not None or reText is not None:
            reWeiboLabel = QtGui.QLabel(reUser + ":" + reText)
            reWeiboLabel.setWordWrap(True)
            mainLayout.addWidget(reWeiboLabel)
        self.setLayout(mainLayout)
