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
query_select_collected_postings_instances = "SELECT PostingID, Posting FROM POSTINGS"
query_select_collected_comments_instances = "SELECT CommentID, Comment FROM COMMENTS"
cursor.execute(query_select_collected_postings_instances)
tuple_collected_postings_instances = cursor.fetchall()      # ((PostingID, Posting), ...)
cursor.execute(query_select_collected_comments_instances)
tuple_collected_comments_instances = cursor.fetchall()      # ((CommentID, Comment), ...)

# posting clean and update
for item in tuple_collected_postings_instances:
    posting = item[1]
    posting = posting.replace("::", " ")
    posting = posting.replace(":", " ")
    posting = posting.strip()

    query_update_pp_posting = f"UPDATE POSTINGS SET PP_Posting = '{posting.lower()}' WHERE PostingID = {item[0]}"
    cursor.execute(query_update_pp_posting)
    # break
    connection.commit()
print('POSTINGS update done')

# comment clean and update
for item in tuple_collected_comments_instances:
    comment = item[1]
    comment = comment.replace("::", " ")
    comment = comment.replace(":", " ")
    comment = comment.strip()

    query_update_pp_comment = f"UPDATE COMMENTS SET PP_Comment = '{comment.lower()}' WHERE CommentID = {item[0]}"
    cursor.execute(query_update_pp_comment)
    # break
    connection.commit()
print('COMMENTS update done')

connection.close()