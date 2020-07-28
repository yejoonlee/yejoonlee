import random
import time
from datetime import datetime, timedelta
import sys
import emoji
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

# DB 커서를 생성해서 수집되어있는 링크와 댓글들을 받아옴
query_select_collected_comments_instances = "SELECT Link, Comment FROM RAW_COMMENTS"
cursor.execute(query_select_collected_comments_instances)
tuple_collected_comments_instances = cursor.fetchall()      # ((link, comment), ...)

# 얼마나 걸리나 보기
start = time.time()

# 활용하기 좋게 dictionary 만들기
dic_collected_comments_instances = {}       # gonna be { link: [comment, ...], ...}
# s = True
# l = ''
for item in tuple_collected_comments_instances:
    # if s:
    #     l = item[0]
    #     s = False
    #
    # #
    try:
        type(dic_collected_comments_instances[item[0]]) != list
    except:
        dic_collected_comments_instances[item[0]] = [item[1]]
        continue
    dic_collected_comments_instances[item[0]].append(item[1])
    # #
    #
    # if item[0] != l:
    #     break
print('dic_collected_comments_instances is made')
# print(dic_collected_comments_instances)
print(time.time()-start)

start = time.time()
# Cleaning first
for link in dic_collected_comments_instances.keys():
    list_processed_comments = []
    for comment in dic_collected_comments_instances[link]:
        comment = comment.replace("::"," ")
        comment = comment.replace(":", " ")
        comment = comment.strip()
        comment = comment.lower()
        list_processed_comments.append(comment)
    dic_collected_comments_instances[link] = list_processed_comments
print('all comments are processed')
# print(dic_collected_comments_instances)
print(time.time()-start)


# AvgLengthComment, NumTag, NumCall, NumComments
dic_link_Nums = {}     # gonna be { link: [AvgLengthComment, NumTag, NumCall, NumComments], ...}
for link in dic_collected_comments_instances.keys():
    sumLengthComments = 0
    numComments = len(dic_collected_comments_instances[link])
    sumNumTag = 0
    sumNumCall = 0
    for comment in dic_collected_comments_instances[link]:
        count = Counter(comment)
        numTag = count["#"]
        numCall = count["@"]
        sumLengthComments += len(comment)
        sumNumTag += numTag
        sumNumCall += numCall

    dic_link_Nums[link] = [round(sumLengthComments/numComments), sumNumTag, sumNumCall, numComments]
    # break

# print(dic_link_Nums)
for link in dic_link_Nums.keys():
    query_insert_instance_RC2PC = f"INSERT INTO POSTINGS_COMMENTS(Link, AvgLengthComment, NumTag, NumCall, NumComments) VALUES ('{link}', {dic_link_Nums[link][0]},{dic_link_Nums[link][1]},{dic_link_Nums[link][2]},{dic_link_Nums[link][3]});"
    cursor.execute(query_insert_instance_RC2PC)
    connection.commit()
    # print(query_insert_instance_RC2PC)
connection.close()