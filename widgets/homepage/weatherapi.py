# -*- coding: UTF-8 -*-
__author__ = 'Maxiee'

import requests
import json
import datetime

def getWeather7Days():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&mode=json&units=metric&cnt=7"

    response = requests.get(url.format('Wuxi'))
    jsonParsed = json.loads(response.text)
    jsonParsed = jsonParsed['list']

    date = []
    minTemp = []
    maxTemp = []
    weather = []

    for i in range(7):
        dayData = jsonParsed[i]
        date.append(datetime.datetime.fromtimestamp(
            dayData['dt']).strftime("%m-%d"))
        minTemp.append(dayData['temp']['min'])
        maxTemp.append(dayData['temp']['max'])
        weather.append(
            translateWeatherDescription(
                dayData['weather'][0]['description']))
    return date, minTemp, maxTemp, weather

def translateWeatherDescription(description):
    dict = {
        "heavy intensity rain": "大暴雨",
        "moderate rain": "中雨",
        "light rain": "小雨",
        "sky is clear": "晴"
    }
    return dict[description]