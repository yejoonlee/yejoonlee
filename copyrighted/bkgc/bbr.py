import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='cxzaqwe3',
                                 db='Archives')
curser = connection.cursor()
import csv
# import time
# from random import uniform
# from selenium import webdriver
# driver_path = '/Users/nezmi/Downloads/chromedriver'
#
# driver = webdriver.Chrome(driver_path)
# driver.get('https://www.ha.com/c/search-results.zx?N=790+231&Nty=1&Ntt=BE%40RBRICK&ic10=ArchiveTab-071515')
# driver.find_element_by_xpath('//*[@id="top"]/div[6]/a[1]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="191846-11078"]/div[2]/a[1]').click()
# # time.sleep(1)
# time.sleep(uniform(10,15))
# driver.find_element_by_xpath('//*[@id="username"]').send_keys('Nezmi')
# time.sleep(uniform(1,2))
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('Iwill0718')
# time.sleep(uniform(2,4))
# driver.find_element_by_xpath('//*[@id="loginButton"]').click()
#
#
# # for elNum in range(300):
# #     elements = driver.find_elements_by_class_name('item-title')
# #     time.sleep(uniform(2, 3))
# #     try:
# #         elements[elNum].click()
# #     except:
# #         print('breaked')
# #         break
# #     time.sleep(uniform(15, 30))
# #     price = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/small[2]/span').text
# #     detailinfo = driver.find_element_by_xpath('//*[@id="auction-description"]/span').text
# #     condition = driver.find_element_by_xpath('//*[@id="condition-report"]').text
# #     query = 'insert into bearbrick (PRICE, etc, cdt) values ("%s","%s","%s");'%(price.replace('"','/'),detailinfo.replace('"','/'),condition.replace('"','/'))
# #     # print(query)
# #     curser.execute(query)
# #     connection.commit()
# #     driver.back()
# #     time.sleep(uniform(2, 4))
#
# time.sleep(uniform(2,4))
# driver.find_element_by_xpath('//*[@id="tabs-1"]/div[4]/a[1]').click()
#
# for elNum in range(26, 100):
#     elements = driver.find_elements_by_class_name('item-title')
#     time.sleep(uniform(2, 3))
#     try:
#         elements[elNum].click()
#     except:
#         print('breaked')
#         break
#     time.sleep(uniform(15, 30))
#     price = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/small[2]/span').text
#     detailinfo = driver.find_element_by_xpath('//*[@id="auction-description"]/span').text
#     condition = driver.find_element_by_xpath('//*[@id="condition-report"]').text
#     query = 'insert into bearbrick (PRICE, etc, cdt) values ("%s","%s","%s");'%(price.replace('"','/'),detailinfo.replace('"','/'),condition.replace('"','/'))
#     # print(query)
#     curser.execute(query)
#     connection.commit()
#     driver.back()
#     time.sleep(uniform(2, 4))
#
# print('GJ')
# driver.close()

# curser.execute('select id,etc from bearbrick')
# data = curser.fetchall()
#
# for d in data:
#     spd = d[1].split('\n')
#     # spspd = spd[1].split(',')
#     for line in spd:
#         if line[:7] == 'Edition':
#             curser.execute('update bearbrick set EDITION = "%s" where id = %d'%(line,d[0]))
#
#     connection.commit()
#     print(d[0])

curser.execute('select ARTIST,TITLE,PRICE,RELEASE_YEAR,MATERIAL,SIZE_TOY,SIZE_BOX,EDITION,cdt,DETAIL from bearbrick')
data = curser.fetchall()

f = open('BE@BRICK.csv','w')
wr = csv.writer(f)
wr.writerow(['콜라보','타이틀','낙찰가격','출시년도','재질','크기','박스크기','에디션','컨디션','정보 디테일'])

for d in data:
    wr.writerow(d)
