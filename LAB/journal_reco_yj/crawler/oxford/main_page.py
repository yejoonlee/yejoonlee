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
cursor.execute('select issn from html')
#issns = cursor.fetchall()
#issns = list(issns)
i = 2
while i <= 26 :
    ii = 1
    while ii < 100:
        try:
            publisher = "oxford academic"
            browser.find_element_by_xpath('//*[@id="ContentColumn"]/div[2]/p[%s]/a[%s]' % (str(i), str(ii))).location_once_scrolled_into_view
            title = browser.find_element_by_xpath('//*[@id="ContentColumn"]/div[2]/p[%s]/a[%s]' % (str(i), str(ii))).text
            browser.find_element_by_xpath('//*[@id="ContentColumn"]/div[2]/p[%s]/a[%s]'%(str(i), str(ii))).click()
            browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/ul/li[2]').location_once_scrolled_into_view
            eissn = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/ul/li[1]').text
            eissn = eissn[12:]
            pissn = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/ul/li[2]').text
            pissn = pissn[11:]
            main_page_html = browser.page_source
            main_page_html = main_page_html.replace("'", "/")
            articles_url = browser.current_url
            #identify = "('"+pissn+"',)"
            #if identify in issns:
            #    cursor.execute("update html set main_page = '%s', journal_title = '%s', publisher = '%s', e_issn = '%s' where issn = '%s'" % (main_page_html, title, publisher, eissn, pissn))
            #    connection.commit()
            #    ii += 1
            #    print(ii+"update")
            #    browser.get("https://academic.oup.com/journals/pages/journals_a_to_z")
            #    continue
            query = "insert into html (issn, e_issn, main_page, articles_url, publisher, journal_title) values ('%s','%s','%s','%s','%s','%s')"%(pissn, eissn, main_page_html, articles_url, publisher, title)
            cursor.execute(query)
            connection.commit()
            browser.get("https://academic.oup.com/journals/pages/journals_a_to_z")
            ii+=1
            print(ii)
            continue
        except:
            print("ee")
            browser.get("https://academic.oup.com/journals/pages/journals_a_to_z")
            ii += 1
            continue
    i += 1

browser.close()
connection.close()