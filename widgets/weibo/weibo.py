__author__ = 'Maxiee'
import os
import json

from PyQt4 import QtCore, QtGui
import requests

from widgets.weibo.ui.WeiboWidget import WeiboWidget


class Constants():
    base_url = "https://api.weibo.com/2/"
    homeline = base_url + "statuses/home_timeline.json?count=%s&page=%s&access_token=%s"


class Weibo(QtGui.QWidget):
    weiboToken = ""

    def __init__(self, parent=None):
        super(Weibo, self).__init__(parent)
        with open(os.path.join(".", "MyData", "config.json")) as f:
            config = json.load(f)
            self.weiboToken = config['weiboToken']
        weiboContent = None
        if self.weiboToken is not "":
            weiboContent = json.loads(self.loadHomeLine(20, 1))
        mainWeibo = QtGui.QWidget(self)
        weiboLayout = QtGui.QVBoxLayout()
        if weiboContent is not None:
            # print(weiboContent) # debug
            weiboContent = weiboContent['statuses']
            for i in range(len(weiboContent)):
                user = weiboContent[i]['user']['name'] + ":"
                text = weiboContent[i]['text']
                reUser = None
                reText = None
                if 'retweeted_status' in weiboContent[i]:
                    reUser = weiboContent[i]['retweeted_status']['user']['name'] + ":"
                    reText = weiboContent[i]['retweeted_status']['text']
                weibo = WeiboWidget(self, user, text, reUser, reText)
                weiboLayout.addWidget(weibo)
        mainWeibo.setLayout(weiboLayout)
        scrollArea = QtGui.QScrollArea()
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scrollArea.setWidgetResizable(False)
        scrollArea.setWidget(mainWeibo)
        mainLayout = QtGui.QVBoxLayout(self)
        mainLayout.addWidget(scrollArea)
        self.setLayout(mainLayout)
        self.setWindowTitle("微博")

    def loadHomeLine(self, count, page):
        response = requests.get(Constants.homeline % (str(count), str(page), self.weiboToken))
        return response.text

