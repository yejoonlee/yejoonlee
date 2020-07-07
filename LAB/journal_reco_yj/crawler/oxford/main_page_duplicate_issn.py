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

browser.get("https://academic.oup.com/journals/pages/journals_a_to_z")
browser.implicitly_wait(3)
cursor.execute("select issn from html where publisher is null")
issns = cursor.fetchall()
issns = list(issns)

i = 2
while i <= 26 :
    ii = 1
    e = 0
    while ii < 100:
        try:
            e = 0
            print(e)
            publisher = "oxford academic"
            browser.find_element_by_xpath('//*[@id="ContentColumn"]/div[2]/p[%s]/a[%s]' % (str(i), str(ii))).location_once_scrolled_into_view
            title = browser.find_element_by_xpath('//*[@id="ContentColumn"]/div[2]/p[%s]/a[%s]' % (str(i), str(ii))).text
            browser.find_element_by_xpath('//*[@id="ContentColumn"]/div[2]/p[%s]/a[%s]'%(str(i), str(ii))).click()
            eissn = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/ul/li[1]').text
            eissn = eissn[12:]
            pissn = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/ul/li[2]').text
            pissn = pissn[11:]
            main_page_html = browser.page_source
            main_page_html = main_page_html.replace("'", "/")
            articles_url = browser.current_url
            for issn in issns:
                issn = str(issn)
                if pissn == issn:
                    cursor.execute("update html set main_page = '%s', journal_title = '%s', publisher = '%s', e_issn = '%s' where issn = '%s'" % (main_page_html, title, publisher, eissn, pissn))
                    connection.commit()
                    print(issn)
                    break
            browser.get("https://academic.oup.com/journals/pages/journals_a_to_z")
            ii+=1
        except:
            print("ee")
            ii += 1
            continue
    i += 1

browser.close()
connection.close()