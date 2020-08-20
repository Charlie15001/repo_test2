import pandas as pd
import time
import csv
import os

# 要搜尋的檔案目錄(所有csv儲存的資料夾內)
file_dir = "D:\\大三下\\GIS競賽\\資料測試\\Taipei_Availability\\"
# 搜尋以.csv為副檔名的檔案
file_ext = r".csv"
file_name = [_ for _ in os.listdir(file_dir) if _.endswith(file_ext)]

path_input = file_dir
path_output = "D:\\大三下\\GIS競賽\\資料測試\\"

# 租借站數量(記得要改成404)
station_num = 10

def create_files(cnt):
    if cnt + 1 < 10:
        with open(path_output + "time_to_column_TPE000{}.csv".format(cnt+1), 'w', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                filewriter.writerow(['Year-Month-Date', 'Hour', 'Minute', 'TimePeriod', 'ServiceAvailable', 'AvailableRentBikes', 'AvailableReturnBikes'])
    elif cnt + 1 < 100:
        with open(path_output + "time_to_column_TPE00{}.csv".format(cnt+1), 'w', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                filewriter.writerow(['Year-Month-Date', 'Hour', 'Minute', 'TimePeriod', 'ServiceAvailable', 'AvailableRentBikes', 'AvailableReturnBikes'])
    else:
        with open(path_output + "time_to_column_TPE0{}.csv".format(cnt+1), 'w', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                filewriter.writerow(['Year-Month-Date', 'Hour', 'Minute', 'TimePeriod', 'ServiceAvailable', 'AvailableRentBikes', 'AvailableReturnBikes'])

def write_files(cnt):
    for i in range(len(file_name)):
        ava = pd.read_csv(file_dir + file_name[i])
        minute = file_name[i][40:42]
        if cnt + 1 < 10:
            with open(path_output + "time_to_column_TPE000{}.csv".format(cnt+1), 'a', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                if ava['ServiceAvailable'][cnt] == 1:
                    if int(ava['SrcUpdateTime'][cnt][11:13]) < 8 or int(ava['SrcUpdateTime'][cnt][11:13]) >= 18:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'night', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                    elif int(ava['SrcUpdateTime'][cnt][11:13]) >= 8 and int(ava['SrcUpdateTime'][cnt][11:13]) <= 12:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'noon', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                    else:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'morning', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                if ava['ServiceAvailable'][cnt] == 0:
                    filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                        ava['SrcUpdateTime'][cnt][11:13], 
                                        minute, 
                                        'NA', 
                                        'NA', 
                                        'NA', 
                                        'NA'])
        elif cnt + 1 < 100:
            with open(path_output + "time_to_column_TPE00{}.csv".format(cnt+1), 'a', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                if ava['ServiceAvailable'][cnt] == 1:
                    if int(ava['SrcUpdateTime'][cnt][11:13]) < 8 or int(ava['SrcUpdateTime'][cnt][11:13]) >= 18:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'night', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                    elif int(ava['SrcUpdateTime'][cnt][11:13]) >= 8 and int(ava['SrcUpdateTime'][cnt][11:13]) <= 12:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'noon', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                    else:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'morning', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                if ava['ServiceAvailable'][cnt] == 0:
                    filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                        ava['SrcUpdateTime'][cnt][11:13], 
                                        minute, 
                                        'NA', 
                                        'NA', 
                                        'NA', 
                                        'NA'])
        else:
            with open(path_output + "time_to_column_TPE0{}.csv".format(cnt+1), 'a', encoding = 'utf-8', newline = '') as f:
                filewriter = csv.writer(f, delimiter = ',')
                if ava['ServiceAvailable'][cnt] == 1:
                    if int(ava['SrcUpdateTime'][cnt][11:13]) < 8 or int(ava['SrcUpdateTime'][cnt][11:13]) >= 18:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'night', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                    elif int(ava['SrcUpdateTime'][cnt][11:13]) >= 8 and int(ava['SrcUpdateTime'][cnt][11:13]) <= 12:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'noon', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                    else:
                        filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                            ava['SrcUpdateTime'][cnt][11:13], 
                                            minute, 
                                            'morning', 
                                            ava['ServiceAvailable'][cnt], 
                                            ava['AvailableRentBikes'][cnt], 
                                            ava['AvailableReturnBikes'][cnt]])
                if ava['ServiceAvailable'][cnt] == 0:
                    filewriter.writerow([ava['SrcUpdateTime'][cnt][0:10], 
                                        ava['SrcUpdateTime'][cnt][11:13], 
                                        minute, 
                                        'NA', 
                                        'NA', 
                                        'NA', 
                                        'NA'])

# main
t1 = time.time()
for i in range(station_num):
    create_files(i)
    write_files(i)
t2 = time.time()
print(t2-t1)