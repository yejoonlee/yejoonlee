import random
import time
from datetime import datetime, timedelta
import sys
sys.path.append('/Users/nezmi/Projects/yeznable_projects')

from LAB.Data_collection import start_selenium
from LAB.Data_collection import functions_for_db
from personal import id_pw_classes

# 이 정보들은 숨길 필요가 있을듯 user_agent는 되도록 그때그때 바꿔주자
root_url = "https://www.instagram.com/"
user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"

insta_class = id_pw_classes.instagram()
ID = insta_class.id_for_crawler
PW = insta_class.pw_for_crawler
target = "kaws"

Driver = start_selenium.Driver(user_agent,root_url)
driver = Driver.start()

# driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')[0].click()
driver.implicitly_wait(5)
time.sleep(5)

# 로그인 정보 입력 및 로그인
driver.find_elements_by_name('username')[0].send_keys(ID)
driver.find_elements_by_name('password')[0].send_keys(PW)
driver.implicitly_wait(5)
time.sleep(6)
driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')[0].click()
driver.implicitly_wait(5)
time.sleep(2)
print('Login...')

# 뭔 알림 설정 취소
driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')[0].click()
driver.implicitly_wait(5)
time.sleep(1)

# 검색창 활성화 하고 검색 입력
driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')[0].click()
driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')[0].send_keys(target)
driver.implicitly_wait(5)
time.sleep(4)

# 검색 결과에서 가장 위에 뜬걸로 들어감
driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div')[0].click()
driver.implicitly_wait(5)
time.sleep(10)
print('Found target...')

# DB에 연결해놓기
# 로그인 정보들 숨길 필요가 있음
mysql_user = id_pw_classes.mysql()

host = '127.0.0.1'
user = mysql_user.id_yeznable
password = mysql_user.pw_yeznable
db = 'KAWS_instagram'

connection = functions_for_db.get_connection(host,user,password,db)
cursor = connection.cursor()
print('DB connected...')

# DB 커서를 생성해서 수집되어있는 링크들을 받아옴
query_select_collected_links = "SELECT link FROM posting_links"
cursor.execute(query_select_collected_links)
tuple_collected_links = cursor.fetchall()
list_collected_links = [list(link)[0] for link in tuple_collected_links]
print(str(len(list_collected_links)) + ' of posting links are collected')

# 마지막 포스트가 2018년 이후 포스트면 계속 돈다
start = True
list_links = []
while True:
    # 페이지의 모든 링크 저장
    elements_links = driver.find_elements_by_tag_name('a')
    new_link_lists = [element.get_attribute('href') for element in elements_links]
    list_links += new_link_lists

    if len(set(list_links) - set(list_collected_links)) < 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        continue

    if start == True:
        print('Collecting...')
        # 처음엔 여러번 스크롤 내림
        # 3번 이상 스크롤을 내리면 한 페이지에 나타나는 링크 수가 60개 정도로 한정되기 때문에
        for i in range(4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            elements_links = driver.find_elements_by_tag_name('a')
            new_link_lists = [element.get_attribute('href') for element in elements_links]
            list_links += new_link_lists
        start = False
    else:
        # 처음 이후로는 한번씩 스크롤 내림
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
    # 적당히 마지막 쪽애 있는 게시물을 열어봄
    driver.implicitly_wait(10)
    driver.find_elements_by_tag_name('a')[45].click()
    time.sleep(4)
    driver.implicitly_wait(5)
    # 2017년 포스트가 나오면 지금까지 포스트들 링크를 전부 저장
    post_time = driver.find_elements_by_tag_name('time')[-1].get_attribute("datetime")
    print(post_time)
    if int(post_time.split('-')[0]) < 2018:
        driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
        elements_links = driver.find_elements_by_tag_name('a')
        new_link_lists = [element.get_attribute('href') for element in elements_links]
        list_links += new_link_lists
        break
    driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()

    list_links_ = list(set(list_links))
    list_links = [link for link in list_links if link.split('/p/')[0] == 'https://www.instagram.com']
    list_links = list(set(list_links) - set(list_collected_links))

    links_for_insert = [f"('{link}')" for link in list_links if link not in list_collected_links]
    for insert in links_for_insert:
        query_for_insert_links = f"INSERT INTO posting_links(link) VALUES {insert};"
        # print(query_for_insert_links)
        cursor.execute(query_for_insert_links)
        connection.commit()

    print(f'{len(links_for_insert)} of postings are collected')

    cursor.execute(query_select_collected_links)
    tuple_collected_links = cursor.fetchall()
    list_collected_links = [list(link)[0] for link in tuple_collected_links]

driver.quit()
connection.close()