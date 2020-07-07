import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()
from selenium import webdriver
import selenium

# browser = webdriver.Chrome("/Users/nezmi/Downloads/chromedriver") #nezmi컴에서 돌릴 때
browser = webdriver.Chrome("C:/Users/USER/Downloads/chromedriver") #서버컴에서 돌릴 때
browser.implicitly_wait(3)

cursor.execute("select articles_url from raw_data where publisher = 'mdpi'")
url_list = cursor.fetchall()
cursor.execute('select title from representative_document')
title_list = cursor.fetchall()
# id = 20000
journal_index = 1
for url in url_list:
    if journal_index < 165:
        journal_index+=1
        continue
    print("journal_index : " + str(journal_index))
    url = str(url)[2:-3]
    browser.get(url)
    browser.implicitly_wait(3)
    cursor.execute("select issn from raw_data where articles_url = '%s'" % url)
    issn = cursor.fetchone()
    cursor.execute("select journal_title from raw_data where articles_url = '%s'" % url)
    journal_title = cursor.fetchone()
    article_index = 1
    while article_index <= 50 :
        try:
            browser.find_element_by_xpath('//*[@id="exportArticles"]/div[%d]/div/a[1]'%article_index).location_once_scrolled_into_view
            browser.find_element_by_xpath('//*[@id="exportArticles"]/div[%d]/div/a[1]'%article_index).click()
            issn = str(issn)[2:-3]
            journal_title = str(journal_title)[2:-3]
            article_url = browser.current_url
            doi = browser.find_element_by_xpath('//*[@id="abstract"]/div[2]/a').text
            title = browser.find_element_by_xpath('//*[@id="abstract"]/h1[1]').text
            if title in title_list:
                continue
            history = browser.find_element_by_xpath('//*[@id="abstract"]/div[7]').text

            abstract = browser.find_element_by_xpath('//*[@id="tabs-0"]/div[1]').text

            keywords = []
            keywords_index = 1
            while keywords_index > 0:
                try:
                    keyword = browser.find_element_by_xpath('//*[@id="tabs-0"]/div[2]/span[2]/a[%d]' %keywords_index).text
                    keywords.append(keyword)
                    keywords_index += 1
                except:
                    break
            str_keywords = ",".join(keywords)

            #html = browser.page_source

            # idx = id + i*10 + ii

            cursor.execute("insert into representative_document (issn, journal_title, doi, title, history, abstract, keywords, article_url) values (' %s ', ' %s ', ' %s ', ' %s ', ' %s ', ' %s ', ' %s ', ' %s ')"%(issn, journal_title, str(doi), str(title), str(history), str(abstract), str_keywords, article_url))
            connection.commit()

            article_index+=1
            print(article_index)
            browser.get(url)
        except selenium.common.exceptions.TimeoutException :
            print("timeout")
            browser.close()
            browser = webdriver.Chrome("C:/Users/USER/Downloads/chromedriver")
            browser.implicitly_wait(3)
            browser.get(url)
            browser.implicitly_wait(5)
            continue
        except :
            article_index+=1
            browser.get(url)
            continue
    journal_index += 1

browser.close()
connection.close()