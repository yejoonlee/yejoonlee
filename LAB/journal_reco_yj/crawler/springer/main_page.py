from selenium import webdriver

# browser = webdriver.Chrome("/Users/nezmi/Downloads/chromedriver") #nezmi컴에서 돌릴 때
browser = webdriver.Chrome("C:/Users/USER/Downloads/chromedriver")
browser.implicitly_wait(3)

import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()
cursor.execute("select issn from raw_data")
issns = cursor.fetchall()

f = open('SearchResults.csv', 'r', encoding='utf-8')
lines = f.readlines()
line_index = 1
for line in lines:
    if line_index < 2358 :
        line_index+=1
        continue
    line = "".join(line)
    line = line.split(',')
    title = line[1]
    url = line[8].replace('"','')
    publisher = "springer"
    try:
        browser.get(url)
    except:
        print(str(line_index)+": skip")
        line_index += 1
        continue
    main_url = browser.current_url
    issn = browser.find_element_by_xpath('//*[@id="issn"]/span[1]').text
    issn = issn[:-8]
    e_issn = browser.find_element_by_xpath('//*[@id="issn"]/span[2]').text
    e_issn = e_issn[:-9]
    main_page = browser.page_source
#    try:
#        numOfarticles = browser.find_element_by_xpath('//*[@id="quick-facts-container"]/ul/li[4]/span[2]').text
#    except:
#        numOfarticles = 0
    for dbissn in issns:
        dbissn = str(dbissn)
        dbissn = dbissn.replace("('","").replace("',)","")
        if dbissn == issn:
            print(issn, dbissn)
            try:
                cursor.execute("update raw_data set main_url = '%s', main_HTML = '%s', journal_title = '%s', publisher = '%s', e_issn = '%s' where issn = '%s'"%(main_url, main_page.replace("'","/"), title, publisher, e_issn, issn))
                connection.commit()
                print('update')
                break
            except:
                continue
    try:
        cursor.execute("insert into html (main_url, journal_title, publisher, issn, e_issn, main_HTML, articles_num) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(main_url, title, publisher, issn, e_issn, main_page.replace("'","/")))
        connection.commit()
    except:
        print(line_index)
        line_index += 1
        continue
    print(line_index)
    line_index+=1

f.close()
browser.close()