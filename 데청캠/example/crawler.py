from selenium import webdriver
from bs4 import BeautifulSoup as bs

# # Task 1
# driver_path = '../resources/chromedriver'
# url = 'https://play.google.com/store/apps/top/category/GAME'
#
# browser = webdriver.Chrome(executable_path=driver_path)
# browser.get(url)
#
# browser.quit()


# # Task 2
# driver_path = '../resources/chromedriver'
# urls = ['https://play.google.com/store/apps/top/category/GAME',
#        'https://www.naver.com/']
#
# browser = webdriver.Chrome(executable_path=driver_path)
# for link in urls:
#     browser.get(link)
#
# browser.quit()

# # # Task 3
#
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">asdfasd
# <a href="http://asdf" class = 'sister' id = "link1">Elsie</a>
# </p></body></html>
# """
#
# soup = bs(html_doc,"html.parser")
# # print(soup.prettify())
#
# # Task 3-1
# tag = soup.a
# print(tag)
# print(tag.name)
# print(tag.attrs)
# print(tag.string)
# print(tag['class'])
#
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup.title.parent.name)
# print(soup.title.parent.title.string)
# print(soup.head.contents[0].string)
#
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link1'))
# print(soup.find(id='link1').string)
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(link['href'])
#
# print(soup.get_text())

# # Task 4
# driver_path = '../resources/chromedriver'
# url = 'https://play.google.com/store/apps/top/category/GAME'
#
# browser = webdriver.Chrome(executable_path=driver_path)
# browser.get(url)
# page = browser.page_source
# browser.quit()
#
# soup = bs(page,"html.parser")
# print(soup.prettify())

# Task 5
import time
driver_path = '../resources/chromedriver'
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path)
browser.get(url)
page = browser.page_source

soup = bs(page,"html.parser")
links = soup.find_all('div',{'class': 'W9yFB'})

disc_links = []

for link in links:
    new_url = link.a['href']
    browser.get('https://play.google.com'+new_url)
    for i in range(3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
    for i in range(1,151):
        try:
            game = browser.find_element_by_xpath(f'//*[@id="fcxH9b"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[{i}]/div/div/div[2]/div/div/div[1]/div/div/div[1]/a').get_attribute('href')
        except:
            print(f'except occur: {i}')
            continue
        disc_links.append(game)
        print(f'collected link: {i}')
    browser.implicitly_wait(5)
    # break

lDisc = []

for i, game in enumerate(disc_links):
    browser.get(game)
    browser.implicitly_wait(3)
    try:
        browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[3]/div/div[1]/div[2]/div[2]/div/span/span').click()
        browser.implicitly_wait(2)
    except:
        pass
    lDisc.append(browser.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > c-wiz:nth-child(1) > c-wiz:nth-child(3) > div > div.W4P4ne > div.PHBdkd > div.DWPxHb > span > div").text)
    print(f'collected page: {i}')

    # if i == 10:
    #     break

browser.quit()
print(lDisc[0])