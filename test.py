# import random
# import time
# from datetime import datetime, timedelta
# import sys
# sys.path.append('/Users/nezmi/Projects/yeznable_projects')
#
# from LAB.Data_collection import start_selenium
# from LAB.Data_collection import functions_for_db
# from personal import id_pw_classes
#
#  # DB에 연결해놓기
# # 로그인 정보들 숨길 필요가 있음
# mysql_user = id_pw_classes.mysql()
#
# host = '127.0.0.1'
# user = mysql_user.id_yeznable
# password = mysql_user.pw_yeznable
# db = 'KAWS_instagram'
#
# # DB 커서를 생성해서 수집된 링크들을 받아옴
# query = "SELECT link FROM posting_links"
#
# connection = functions_for_db.get_connection(host,user,password,db)
# cursor = connection.cursor()
# print('DB connected...')
# cursor.execute(query)
# tuple_link_collected = cursor.fetchall()
# list_link_collected = [list(link)[0] for link in tuple_link_collected]
#
# print(str(len(list_link_collected)) + ' of posting links are collected')
# print('acctualy ' + str(len(set(list_link_collected))) + ' of posting links are collected')

import emoji
print(emoji.demojize('✌️🇯🇵  # Repost @kyoko1903 ・・・ M'))
