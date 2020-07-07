import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()
from selenium import webdriver

browser = webdriver.Chrome("C:/Users/USER/Downloads/chromedriver")
browser.implicitly_wait(3)

browser.get("http://www.mdpi.com/about/journals")
browser.implicitly_wait(3)
i = 196
while i <= 200 :
#        try:
            browser.find_element_by_xpath('//*[@id="journaltable"]/tbody/tr[%d]/td[3]'%(i+1)).location_once_scrolled_into_view
            issn = browser.find_element_by_xpath('//*[@id="journaltable"]/tbody/tr[%d]/td[3]'%i).text
            articles_num = browser.find_element_by_xpath('//*[@id="journaltable"]/tbody/tr[%d]/td[7]/a'%i).text
            browser.find_element_by_xpath('//*[@id="journaltable"]/tbody/tr[%d]/td[7]/a'%i).click()
            articles_url = browser.current_url
            cursor.execute('update html set articles_url = %s, articles_num = %s where issn = %s',(articles_url, articles_num, issn))
            connection.commit()
            print(i)
            i+=1
            browser.get("http://www.mdpi.com/about/journals")
#        except:
#            break

browser.close()
connection.close()