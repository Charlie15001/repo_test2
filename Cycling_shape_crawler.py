import json
from selenium import webdriver
from bs4 import BeautifulSoup

path = 'D:\\大三下\\GIS競賽\\資料蒐集\\自行車道資料\\'
city = 'Taipei'

driver = webdriver.Chrome()
api_Cycling_shape = "https://ptx.transportdata.tw/MOTC/v2/Cycling/Shape/Taipei?$format=JSON"

driver.get(api_Cycling_shape)

soup_Cycling_shape = BeautifulSoup(driver.page_source, 'lxml')
soup_Cycling_shape_text = soup_Cycling_shape.find('pre').text
#print(soup_Cycling_shape_text)
Cycling_shape_json = json.loads(soup_Cycling_shape_text)

with open('{path}{city}_Cycling_Shape.json'.format(path = path, city = city), 'w') as f:
    json.dump(Cycling_shape_json, f)