print('hello python & git rock')

from selenium import webdriver
driver = webdriver.Chrome()

api_raininfo = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization=CWB-E9CFB481-091B-449F-9A6A-F0EA269D8DB6"

driver.get(api_raininfo)