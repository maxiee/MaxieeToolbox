# -*- coding: UTF-8 -*-
__author__ = 'Maxiee'

import requests
import json
import datetime

def getWeather7Days():
    date = []
    minTemp = []
    maxTemp = []
    weather = []
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&mode=json&units=metric&cnt=7"
    try:
        response = requests.get(url.format('Wuxi'))
    except requests.RequestException:
        return False, date, minTemp, maxTemp, weather

    try:
        jsonParsed = json.loads(response.text)
        jsonParsed = jsonParsed['list']
    except ValueError:
        return False, date, minTemp, maxTemp, weather

    for i in range(7):
        dayData = jsonParsed[i]
        date.append(datetime.datetime.fromtimestamp(
            dayData['dt']).strftime("%m-%d"))
        minTemp.append(dayData['temp']['min'])
        maxTemp.append(dayData['temp']['max'])
        weather.append(
            translateWeatherDescription(
                dayData['weather'][0]['description']))
    return True, date, minTemp, maxTemp, weather

def translateWeatherDescription(description):
    dict = {
        "heavy intensity rain": "大暴雨",
        "moderate rain": "中雨",
        "light rain": "小雨",
        "sky is clear": "晴",
        "scattered clouds": "多云",
        "few clouds": "少云"
    }
    return dict[description]