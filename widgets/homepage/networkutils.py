__author__ = 'Maxiee'
import os
import json

import requests


def connectNetwork():
    url = "http://210.28.18.6:801/eportal/?c=ACSetting&a=Login&wlanuserip=null&wlanacip=null&wlanacname=null&port=&iTermType=1&session=ac150d18-000000000000-0000"
    with open(os.path.join(".", "MyData", "config.json")) as f:
        config = json.load(f)
        account = config['netAccount']
        password = config['netPassword']
        payload = {
            "DDDDD": account,
            "upass": password,
            "R1": "0",
            "R6": "0",
            "para": "00",
            "0MKKey": "123456"
        }
        response = requests.post(url, data=payload)
        print(response.text)

