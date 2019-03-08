import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='cxzaqwe3',
                                 db='Archives')

curser = connection.cursor()

import time
from random import *

# f = open('./ㅁㄴㅇㄹ.txt')
# text = f.read()
# lurl = text.split('\n')
# print(lurl)

from selenium import webdriver

driver_path = '/Users/nezmi/Downloads/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get('https://fineart.ha.com/c/recent-bid-activity.zx?saleNo=191846&ic5=CatalogHome-ActionArea-MostRecentBidActivity-052316')
for i in range(150):
    i = i+1
    title = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[4]/div/div/table/tbody/tr[%d]/td[2]/a'%i).text
    bid = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[4]/div/div/table/tbody/tr[%d]/td[3]'%i).text
    log = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[4]/div/div/table/tbody/tr[%d]/td[4]'%i).text
    # print(title+'\n'+lot+'\n'+bid)
    query = 'insert into bid_log (SHORT_DESCRIPTION, CURRENT_BID, BID_TIME) values ("%s","%s","%s");'%(title,bid,log)
    # print(query)
    curser.execute(query)
    connection.commit()
    print('%d: OK'%i)
driver.close()