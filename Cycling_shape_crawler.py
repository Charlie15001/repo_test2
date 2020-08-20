import json
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

path = 'D:\\大三下\\GIS競賽\\資料蒐集\\自行車道資料\\'
city = 'NewTaipei'

driver = webdriver.Chrome()
api_Cycling_shape = "https://ptx.transportdata.tw/MOTC/v2/Cycling/Shape/NewTaipei?$format=JSON"

driver.get(api_Cycling_shape)

soup_Cycling_shape = BeautifulSoup(driver.page_source, 'lxml')
soup_Cycling_shape_text = soup_Cycling_shape.find('pre').text
#print(soup_Cycling_shape_text)
Cycling_shape_json = json.loads(soup_Cycling_shape_text)

with open('{path}{city}_Cycling_Shape.json'.format(path = path, city = city), 'w') as f:
    json.dump(Cycling_shape_json, f)

with open('{path}{city}_Cycling_Shape.csv'.format(path = path, city = city), 'w', encoding = 'utf-8', newline = '') as f:
    filewriter = csv.writer(f, delimiter = ',')
    filewriter.writerow(['RouteName', 
                        'CityCode', 
                        'City',  
                        'Geometry',  
                        'UpdateTime'])

with open('{path}{city}_Cycling_Shape.csv'.format(path = path, city = city), 'a', encoding = 'utf-8', newline = '') as f:
    filewriter = csv.writer(f, delimiter = ',')
    for i in range(len(Cycling_shape_json)):
        filewriter.writerow([Cycling_shape_json[i]['RouteName'], 
                            Cycling_shape_json[i]['CityCode'], 
                            Cycling_shape_json[i]['City'], 
                            Cycling_shape_json[i]['Geometry'],  
                            Cycling_shape_json[i]['UpdateTime']])