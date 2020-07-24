import random
import time
from datetime import datetime, timedelta
import sys
import emoji
sys.path.append('/Users/nezmi/Projects/yeznable_projects')

from LAB.Data_collection import start_selenium
from LAB.Data_collection import functions_for_db
from personal import id_pw_classes

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
query_select_collected_links = "SELECT Link FROM POSTING_LINKS"
query_select_collected_postings_links = "SELECT Link FROM COMMENTS"
cursor.execute(query_select_collected_links)
tuple_collected_links = cursor.fetchall()
cursor.execute(query_select_collected_postings_links)
tuple_collected_comments_links = cursor.fetchall()
list_collected_links = [list(link)[0] for link in tuple_collected_links]
set_collected_comments_links = set([list(link)[0] for link in tuple_collected_comments_links])
target_links = list(set(list_collected_links)-set_collected_comments_links)
print(str(len(target_links)) + ' of posting links to collect')

# 이 정보들은 숨길 필요가 있을듯 user_agent는 되도록 그때그때 바꿔주자
root_url = "https://www.instagram.com/"
user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"

insta_class = id_pw_classes.instagram()
ID = insta_class.id_for_crawler
PW = insta_class.pw_for_crawler

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
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
driver.implicitly_wait(5)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
driver.implicitly_wait(5)
time.sleep(1)

# 링크들을 전부 돌아다니면서 정보수집
for link in target_links:
    # 타겟 데이터 찾고 필요한 모양으로 전처리
    driver.get(link)
    driver.implicitly_wait(5)
    time.sleep(1)

    element_comments = driver.find_elements_by_class_name('C4VMK')[1:]
    # print(element_comments)

    # comments 다 나오도록 버튼 누르기
    comments_last = ['']
    # no_comments = False
    while True:
        try:
            driver.find_element_by_class_name('dCJp8').click()
            driver.implicitly_wait(3)
            time.sleep(1)
        except:
            driver.implicitly_wait(5)
            time.sleep(5)
            pass

        comments_now = driver.find_elements_by_class_name('C4VMK')[1:]
        # try:
        #     if comments_last[-1] == comments_now[-1]:
        #         break
        # except:
        #     no_comments = True
        #     print(link)
        #     break
        if comments_last[-1] == comments_now[-1]:
            break
        comments_last = comments_now

    # if no_comments:
    #     continue

    # comments 수집
    element_comments = driver.find_elements_by_class_name('C4VMK')[1:]
    list_comments = []
    for element in element_comments:
        comment = element.text.split('\n')[1]
        if comment == '인증됨':
            comment = element.text.split('\n')[2]
        list_comments.append(comment)

    print(str(len(list_comments)) + ' of commnets are collected this time')
    list_comments = list(set(list_comments))


    # DB에 데이터 저장
    for single_comment in list_comments:
        single_comment = emoji.demojize(single_comment)
        single_comment = single_comment.replace("'", ' ')
        single_comment = single_comment.replace('"', ' ')
        query_for_insert_data = f"INSERT INTO COMMENTS(Link, Comment) VALUES ('{link}', '{single_comment}');"
        try:
            cursor.execute(query_for_insert_data)
        except:
            print(link)
            print(query_for_insert_data)
        connection.commit()
    # break

driver.quit()
connection.close()