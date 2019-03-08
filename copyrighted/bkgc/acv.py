import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='cxzaqwe3',
                                 db='Archives')

curser = connection.cursor()

import time
from random import *

f = open('./ㅁㄴㅇㄹ.txt')
text = f.read()
lurl = text.split('\n')
# print(lurl)

from selenium import webdriver

driver_path = '/Users/nezmi/Downloads/chromedriver'
for i,url in enumerate(lurl):
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    time.sleep(uniform(15,60))
    title = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/h1/i').text
    artist = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/h1').text
    artist = artist.split('.')[0]
    bid = driver.find_element_by_xpath('//*[@id="bidBlockTop"]/span/strong').text
    # print(title+'\n'+lot+'\n'+bid)
    driver.close()

    query = "update 2018_November_7_The_Toy_Collection_of_Ronnie_K_Pirovino_191846 set BID_D_1 = %s where TITLE like '%s' and ARTIST like '%s';"%(bid[1:].replace(',',''),'%'+title+'%','%'+artist+'%')
    # print(query)
    try:
        curser.execute(query)
        connection.commit()
        print('%d: OK'%i)
    except:
        print(url)