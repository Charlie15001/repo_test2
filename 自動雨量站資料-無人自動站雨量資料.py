#!/usr/bin/env python
# coding: utf-8

# In[1]:
try:

    import csv
    import json
    import datetime
    from bs4 import BeautifulSoup
    from selenium import webdriver


    # In[3]:


    driver = webdriver.Chrome()
    api_raininfo = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization=CWB-E9CFB481-091B-449F-9A6A-F0EA269D8DB6"

    driver.get(api_raininfo)


    # In[4]:


    raininfo = driver.page_source
    #print(weatherinfo)


    # In[5]:


    soup_Raininfo = BeautifulSoup(driver.page_source, 'lxml')
    raininfo_text = soup_Raininfo.find('pre').text
    #print(weatherinfo_text)


    # In[6]:


    now = datetime.datetime.now() #現在時間

    date_time = now.strftime("%Y%m%d%H%M%S")
    print(date_time)


    # In[8]:


    raininfo_data = json.loads(raininfo_text)
    #print(weatherinfo_data)


    # In[18]:


    #print(weatherinfo_data['records']['location'])


    # In[20]:


    with open('D:\\大三下\\GIS競賽\\資料蒐集\\氣象資料\\Taiwan_Weatherinfo_data_{}.json'.format(int(date_time)), 'w') as f:
        json.dump(raininfo_data['records']['location'], f)

    with open('D:\\大三下\\GIS競賽\\資料蒐集\\氣象資料\\Taiwan_Weatherinfo_data_{}.json'.format(int(date_time)), 'r') as f:
        raininfo_data['records']['location'] = json.load(f)

except Exception as e:
    from linebot import LineBotApi
    from linebot.models import TextSendMessage
    line_bot_api = LineBotApi('S0SQxbiNe5IpLK77sfuGbJEFY9G0VEeQ/oCQwVNZ125Rc86w2liPLZcOcB/ek8c0MTNE7uL67rDhbzDayucZfShpiWlR1sLwTqOED6e+OoNfjgE8Oo7rvu8/vU8CBMxMvHExLdF8z0h3PzlUg2AQwQdB04t89/1O/w1cDnyilFU=')

    #push message to one user
    line_bot_api.push_message('Udf62ccd519421611ccde232bcadda55a', 
        TextSendMessage(text = 'Something went wrong, please check it as soon as possible. ' + str(e) +' From 雨量資料'))

# In[ ]:




