__author__ = 'Maxiee'
from PyQt4 import QtCore, QtGui
import os
import json
import requests


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
        weiboLayout = QtGui.QVBoxLayout()
        if weiboContent is not None:
            weiboContent = weiboContent['statuses']
            for i in range(len(weiboContent)):
                str = weiboContent[i]['user']['name'] + ":"
                str += weiboContent[i]['text']
                if 'retweeted_status' in  weiboContent[i]:
                    str += "转发自"
                    str += weiboContent[i]['retweeted_status']['user']['name'] + ":"
                    str += weiboContent[i]['retweeted_status']['text']
                weiboLayout.addWidget(QtGui.QLabel(str))
        self.setLayout(weiboLayout)
        self.setWindowTitle("微博")

    def loadHomeLine(self, count, page):
        response = requests.get(Constants.homeline % (str(count), str(page), self.weiboToken))
        return response.text

