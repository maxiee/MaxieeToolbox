# -*- coding: UTF-8 -*-
__author__ = 'Maxiee'

import json
import datetime

import requests


def getWeather7Days():
    date = []
    minTemp = []
    maxTemp = []
    weather = []
    url = "http://api.openweathermap.org/data/2.5/forecast?lat=31.57&lon=120.29&units=metric"
    # 调用这个接口才会得到正确信息：
    # http://api.openweathermap.org/data/2.5/forecast?lat=31.57&lon=120.29&units=metric
    try:
        response = requests.get(url)
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
            dayData['dt']).strftime("%m-%d-%H"))
        minTemp.append(dayData['main']['temp_min'])
        maxTemp.append(dayData['main']['temp_max'])
        weather.append(
            translateWeatherDescription(
                dayData['weather'][0]['description']))
    return True, date, minTemp, maxTemp, weather


def translateWeatherDescription(description):
    dict = {
        "very heavy rain": "大暴雨",
        "heavy intensity rain": "暴雨",
        "moderate rain": "中雨",
        "light rain": "小雨",
        "sky is clear": "晴",
        "scattered clouds": "多云",
        "few clouds": "少云",
        "broken clouds": "阴转晴"
    }
    try:
        return dict[description]
    except KeyError:
        return description