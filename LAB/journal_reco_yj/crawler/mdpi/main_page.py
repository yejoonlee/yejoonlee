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
i = 1
while i <= 200 :
        try:
            publisher = "mdpi"
            issn = browser.find_element_by_xpath('//*[@id="journaltable"]/tbody/tr[%d]/td[3]'%i).text
            title = browser.find_element_by_xpath('//*[@id="journaltable"]/tbody/tr[%d]/td[2]/a'%i).text
            browser.find_element_by_xpath('//*[@id="journaltable"]/tbody/tr[%d]/td[2]/a'%i).click()
            main_page = browser.page_source
            cursor.execute('select issn from html')
            issns = cursor.fetchall()
            if issn in issns:
                cursor.execute("update html set main_page = '%s', journal_title = '%s', publisher = '%s' where issn = '%s'" %(main_page, title, publisher, issn))
                connection.commit()
                i += 1
                browser.get("http://www.mdpi.com/about/journals")
                continue
            try:
                cursor.execute("insert into html (issn, main_page, journal_title, publisher) values ('%s', '%s', '%s', '%s')" %(issn, main_page, title, publisher))
            except:
                i += 1
                browser.get("http://www.mdpi.com/about/journals")
                continue
            connection.commit()
            i+=1
            browser.get("http://www.mdpi.com/about/journals")
        except:
            break

browser.close()
connection.close()