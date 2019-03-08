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
    try:
        driver.get(url)
    except:
        print('%d: end?'%i)
        continue
    time.sleep(uniform(15,30))
    driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/small[2]/a[1]').click()
    time.sleep(uniform(15,30))
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('Nezmi')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('Iwill0718')
    driver.find_element_by_xpath('//*[@id="loginButton"]').click()

    title = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/h1/i').text
    artist = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/h1').text
    artist = artist.split('.')[0]
    price = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/small[2]/span').text
    # print(title+'\n'+lot+'\n'+bid)
    driver.close()

    query = "update 2018_November_7_The_Toy_Collection_of_Ronnie_K_Pirovino_191846 set FINAL_PRICE = '%s' where TITLE like '%s' and ARTIST like '%s';"%(price[1:],'%'+title+'%','%'+artist+'%')

    # print(query)
    #
    # if i > 1:
    #     break

    try:
        curser.execute(query)
        connection.commit()
        print('%d: %s'%(i,title))
    except:
        print(url)