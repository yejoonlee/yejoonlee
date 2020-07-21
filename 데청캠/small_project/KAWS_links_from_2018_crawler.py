import random
import time
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

# 마지막 포스트가 2018년 이후 포스트면 계속 돈다
while True:
    # 스크롤 내림
    # 가장 마지막 게시물을 열어봄
    driver.find_elements_by_class_name('v1Nh3 KIKUG  _bz0w')[-1].click()
    if driver.find_elements_by_class_name('_1o9PC Nzb55').get_attribute("datetime") < 2018:
        asdf = 0
    # 2017년 포스트가 나오면 지금까지 포스트들 링크를 전부 저장

# DB에 연결해놓기
# 로그인 정보들 숨길 필요가 있음
host = '127.0.0.1'
user = 'yeznale'
password = 'cxzaqwe3'
db = 'KIC'

# # DB 커서를 생성해서 수집된 링크들을 받아옴
# query = "SELECT feed_link FROM Raw"
#
# connection = functions_for_db.get_connection(host,user,password,db)
# cursor = connection.cursor()
# print('DB connected...')
# cursor.execute(query)
# tCollected = cursor.fetchall()
# lCollected = [list(link)[0] for link in tCollected]
# print(str(len(lCollected)) + ' of feed links are collected')
#
# condition = True
# button_switch = ''
# while condition:
#     link_now = driver.current_url.split('/')[-2]
#
#     # 첫 번째 글이 이미 수집된거면 수집된 링크의 수 만큼 스킵한다. 뒤에 if 문이 있는데 이게 쓸모가 있는건 지 없는 건지는 모르겠다.
#     if link_now == lCollected[0]:
#         for i in range(len(lCollected)):
#             print('Skipping feed already be collected...')
#             driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/a%s' % button_switch)[0].click()
#             if button_switch == '':
#                 button_switch = '[2]'
#             driver.implicitly_wait(5)
#             time.sleep(random.randrange(1.0,2.0))
#             continue
#
#     if link_now in lCollected:
#         # 수집된 링크라면 다음 글로 넘어감
#         print('Feed already be collected...')
#         driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/a%s'%button_switch)[0].click()
#         if button_switch == '':
#             button_switch = '[2]'
#         driver.implicitly_wait(5)
#         time.sleep(random.randrange(1.0,2.0))
#         continue
#     else:
#         # 수집되지 않은 링크라면 DB에 추가
#         cursor.execute("INSERT INTO Raw(feed_link) VALUES ('%s')" %link_now)
#         connection.commit()
#         print('%s collected' %link_now)
#         # 다음 글로 넘어감
#         driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/a%s'%button_switch)[0].click()
#         if button_switch == '':
#             button_switch = '[2]'
#         driver.implicitly_wait(10)
#         time.sleep(random.randrange(3.0,6.0))