#!/usr/bin/env python
# coding: utf-8
#D:\00課程\大二下學期\競賽\py-crawer\tc-bike-ava-loop.py
# In[55]:
import time
import json
from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint
import csv

###APP ID：
#APP Key：
app_id = '1f48e6c1449f4b0d910e3fe875fc73d7'
app_key = 'iXELUTA5llKxwmTS4acpD9yOwiA'

##########################不同城市在改在city#########################
#CITY
city = "Taipei" #或是 "Taichung", "Tainan"
#Request url
url = "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/" + city + "?$format=JSON"
#Path
path = "D:/00課程/大二下學期/競賽/bike-ava-output/"

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'utf-8'
        }

try:
    for x in range (2):
        if __name__ == '__main__':
            a = Auth(app_id, app_key)
            response = request('get', url, headers= a.get_auth_header())
            #pprint(response.content) #response.content為bytes
            response_str = response.content.decode() #bytes to string
            response_json = json.loads(response_str) #string to list

            now = datetime.now() #現在時間
            date_time = now.strftime("%Y%m%d%H%M%S")
            #print(date_time)

            #存成json
            with open('{path}{city}_Bike_Availability_{time}.json'.format(path = path, city = city, time = int(date_time)), 'w') as f:
                json.dump(response_json, f)
            #存成csv
            with open('{path}{city}_Bike_Availibility_test_{time}.csv'.format(path = path, city = city, time = int(date_time)), 'w', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                filewriter.writerow(['StationUID', 
                                    'ServiceAvailable', 
                                    'AvailableRentBikes', 
                                    'AvailableReturnBikes', 
                                    'SrcUpdateTime'])
            with open('{path}{city}_Bike_Availibility_test_{time}.csv'.format(path = path, city = city, time = int(date_time)), 'a', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                for i in range(len(response_json)):
                    filewriter.writerow([response_json[i]['StationUID'], 
                                        response_json[i]['ServiceAvailable'], 
                                        response_json[i]['AvailableRentBikes'], 
                                        response_json[i]['AvailableReturnBikes'], 
                                        response_json[i]['SrcUpdateTime']])
            #全部資料整理成一個檔案
            with open('{path}{city}_Bike_Availibility_All.csv'.format(path = path, city = city), 'a', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                for i in range(len(response_json)):
                    filewriter.writerow([response_json[i]['StationUID'], 
                                        response_json[i]['ServiceAvailable'], 
                                        response_json[i]['AvailableRentBikes'], 
                                        response_json[i]['AvailableReturnBikes'], 
                                        response_json[i]['SrcUpdateTime']])
            #加條件避免整個程式跑完會再停滯121sec
            if x < 1:
                time.sleep(121)
except Exception as e:
    from linebot import LineBotApi
    from linebot.models import TextSendMessage
    line_bot_api = LineBotApi('S0SQxbiNe5IpLK77sfuGbJEFY9G0VEeQ/oCQwVNZ125Rc86w2liPLZcOcB/ek8c0MTNE7uL67rDhbzDayucZfShpiWlR1sLwTqOED6e+OoNfjgE8Oo7rvu8/vU8CBMxMvHExLdF8z0h3PzlUg2AQwQdB04t89/1O/w1cDnyilFU=')

    #push message to one user
    #自動報錯
    line_bot_api.push_message('Udf62ccd519421611ccde232bcadda55a', 
        TextSendMessage(text = 'Something went wrong, please check it as soon as possible. ' + str(e) +' From 自行車資料'))