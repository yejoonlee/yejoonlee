from Data_collection import start_selenium
from Data_collection import functions_for_db

# # DB에 연결해놓기
# # 로그인 정보들 숨길 필요가 있음
# host = '127.0.0.1'
# user = 'root'
# password = 'cxzaqwe3'
# db = 'KIC'
#
# # DB 커서를 생성해서 수집된 링크들을 받아옴
# connection = functions_for_db.get_connection(host,user,password,db)
# cursor = connection.cursor()
# cursor.execute("SELECT id, feed_link FROM Raw")
# tCollected = cursor.fetchall()
# lCollected = [list(str) for str in tCollected]
# print('DB connected...')
# print(lCollected)
#
# for i in lCollected:
#     query = "UPDATE Raw SET feed_link = '%s' WHERE id = %s" %(i[1].split('/')[-2],str(i[0]))
#     cursor.execute(query)
#     connection.commit()

#
#
#
# teststr = 'https://www.instagram.com/p/ByXbZkjjl7w/?utm_source=ig_web_copy_link'
#
# if teststr in lCollected:
#     print('Y')
# else:
#     print('N')

# # 이 정보들은 숨길 필요가 있을듯 user_agent는 되도록 그때그때 바꿔주자
# root_url = "https://www.instagram.com/"
# user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
# ID = "yejoonlee617@gmail.com"
# PW = "Cxzasd321!"
# target = "kaws"
#
# Driver = start_selenium.Driver(user_agent,root_url)
# driver = Driver.start()
#
# print(driver.current_url)



for i in range(5):
    print(i)


<span class="glyphsSpriteCircle_add__outline__24__grey_9 u-__7" aria-label="Load more comments"></span>

< span class ="glyphsSpriteCircle_add__outline__24__grey_9 u-__7" aria-label="Load more comments" > < / span >


< a class ="notranslate" href="/christian_royce/" > @ christian_royce < / a >