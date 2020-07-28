from pycaret.nlp import *
import numpy as np
import sys
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

# DB 커서를 생성해서 수집되어있는 댓글들과 ID를 받아옴
query_select_collected_comments_instances = "SELECT CommentID, PP_Comment FROM COMMENTS"
cursor.execute(query_select_collected_comments_instances)
tuple_collected_comments_instances = cursor.fetchall()      # ((CommentID, PP_Comment), ...)

dic_collected_comments_instances = {}
for item in tuple_collected_comments_instances:
    dic_collected_comments_instances[item[0]] = item[1].encode('utf8')
print(list(dic_collected_comments_instances.values())[0])

data = np.array(list(dic_collected_comments_instances.values()))
print(data.dtype)
dt = {'names':['Comments'], 'formats':['|S2453']}
data.dtype = dt

print(data['Comments'])
# nlp1 = setup(data, session_id = 123)