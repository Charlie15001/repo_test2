try:
    import csv
    import json
    import datetime
    import requests

    path = 'D:\\大三下\\GIS競賽\\資料蒐集\\氣象資料\\'

    api_raininfo = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization=CWB-E9CFB481-091B-449F-9A6A-F0EA269D8DB6'
    api_weatherinfo = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-E9CFB481-091B-449F-9A6A-F0EA269D8DB6'

    response_raininfo = requests.get(api_raininfo)
    response_weatherinfo = requests.get(api_weatherinfo)

    now = datetime.datetime.now() #現在時間
    date_time = now.strftime("%Y%m%d%H%M%S")
    print(int(date_time))

    #str to json
    response_raininfo_json = json.loads(response_raininfo.text)
    response_weatherinfo_json = json.loads(response_weatherinfo.text)

    #open a json file
    with open('{path}Taiwan_Raininfo_data_{date_time}.json'.format(path = path, date_time = int(date_time)), 'w') as f:
        json.dump(response_raininfo_json['records']['location'], f)
    with open('{path}Taiwan_Weatherinfo_data_{date_time}.json'.format(path = path, date_time = int(date_time)), 'w') as f:
        json.dump(response_weatherinfo_json['records']['location'], f)

except Exception as e:
    from linebot import LineBotApi
    from linebot.models import TextSendMessage
    line_bot_api = LineBotApi('S0SQxbiNe5IpLK77sfuGbJEFY9G0VEeQ/oCQwVNZ125Rc86w2liPLZcOcB/ek8c0MTNE7uL67rDhbzDayucZfShpiWlR1sLwTqOED6e+OoNfjgE8Oo7rvu8/vU8CBMxMvHExLdF8z0h3PzlUg2AQwQdB04t89/1O/w1cDnyilFU=')

    #push message to one user
    line_bot_api.push_message('Udf62ccd519421611ccde232bcadda55a', 
        TextSendMessage(text = 'Something went wrong, please check it as soon as possible. ' + str(e) +' From 氣象&雨量資料'))

    
