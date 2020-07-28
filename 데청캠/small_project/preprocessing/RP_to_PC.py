import random
import time
from datetime import datetime, timedelta
import sys
from collections import Counter
sys.path.append('/Users/nezmi/Projects/yeznable_projects')

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

# DB 커서를 생성해서 수집되어있는 링크와 포스팅 정보들을 받아옴
query_select_collected_postings_instances = "SELECT Link, Number_of_like, PostDate, PP_Posting FROM POSTINGS ORDER BY PostDate DESC"
cursor.execute(query_select_collected_postings_instances)
tuple_collected_postings_instances = cursor.fetchall()      # ((Link, Number_of_like, PostDate, Posting), ...)

query_select_target_links_instances = "SELECT Link FROM POSTINGS_COMMENTS"
cursor.execute(query_select_target_links_instances)
tuple_collected_target_links_instances = cursor.fetchall()      # ((Link), ...)


# 활용하기 좋게 dictionary 만들기
dic_collected_postings_instances = {}       # gonna be { link: [Number_of_like, PostDate, PP_Posting], ...}
for item in tuple_collected_postings_instances:
    dic_collected_postings_instances[item[0]] = list(item[1:])
    # break
# print(dic_collected_postings_instances)
print('dic_collected_postings_instances is made')

# # Term_from_Last
# for instance in dic_collected_postings_instances.values():
#     PostDate = instance[1]

# # NumLike, LengthPost, PostedYear
# dic_link_Nums = {}     # gonna be { link: [NumLike, LengthPost, PostedYear], ...}
# for target_link in tuple_collected_target_links_instances:
#     for link in dic_collected_postings_instances.keys():
#         if link == target_link[0]:
#             NumLike = dic_collected_postings_instances[link][0]
#             LengthPost = len(dic_collected_postings_instances[link][2])
#             PostedYear = str(dic_collected_postings_instances[link][1]).split('-')[0]
#
#             dic_link_Nums[link] = [NumLike, LengthPost, int(PostedYear)]
#         else:
#             continue
#         # break
# # print(dic_link_Nums)
#
# for link in dic_link_Nums.keys():
#     query_update_instance_RP2PC = f"UPDATE POSTINGS_COMMENTS SET NumLike = {dic_link_Nums[link][0]}, LengthPost = {dic_link_Nums[link][1]}, PostedYear = {dic_link_Nums[link][2]} WHERE Link = '{link}'"
#     cursor.execute(query_update_instance_RP2PC)
#     connection.commit()
#     # print(query_update_instance_RP2PC)
#     # break
# connection.close()

# P_NumTag, P_NumCall
dic_link_Nums = {}     # gonna be { link: [P_NumTag, P_NumCall], ...}
for target_link in tuple_collected_target_links_instances:
    for link in dic_collected_postings_instances.keys():
        if link == target_link[0]:
            count = Counter(dic_collected_postings_instances[link][2])
            P_NumTag = count["#"]
            P_NumCall = count["@"]

            dic_link_Nums[link] = [P_NumTag, P_NumCall]
        else:
            continue
        # break

for link in dic_link_Nums.keys():
    query_update_instance_RP2PC = f"UPDATE POSTINGS_COMMENTS SET P_NumTag = {dic_link_Nums[link][0]}, P_NumCall = {dic_link_Nums[link][1]} WHERE Link = '{link}'"
    cursor.execute(query_update_instance_RP2PC)
    connection.commit()
    # print(query_update_instance_RP2PC)
    # break
connection.close()