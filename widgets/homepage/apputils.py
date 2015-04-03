__author__ = 'Maxiee'
import os
import json


class MyApps():
    def __init__(self):
        with open(os.path.join(".", "MyData", "myapps.json"), encoding="utf8") as f:
            self.myAppsData = json.load(f)
            self.index = 0

    def fetchOneCategory(self):
        if not self.index < len(self.myAppsData):
            return None, None
        catagory = self.myAppsData[self.index]['category']
        apps = self.myAppsData[self.index]['apps']
        self.index += 1
        return catagory, apps