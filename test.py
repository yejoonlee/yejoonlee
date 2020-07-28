# import sys
# from collections import Counter
# sys.path.append('/Users/nezmi/Projects/yeznable_projects')
#
# from LAB.Data_collection import functions_for_db
# from personal import id_pw_classes
#
# # DB에 연결해놓기
# # 로그인 정보들 숨길 필요가 있음
# mysql_user = id_pw_classes.mysql()
#
# host = '127.0.0.1'
# user = mysql_user.id_yeznable
# password = mysql_user.pw_yeznable
# db = 'KAWS_instagram'
#
# connection = functions_for_db.get_connection(host,user,password,db)
# cursor = connection.cursor()
# print('DB connected...')
#
# # DB 커서를 생성해서 수집되어있는 링크와 포스팅 정보들을 받아옴
# query_select_collected_postings_instances = "SELECT Link, Number_of_like, PostDate, Posting FROM POSTINGS ORDER BY PostDate DESC"
# cursor.execute(query_select_collected_postings_instances)
# tuple_collected_postings_instances = cursor.fetchall()      # ((Link, Number_of_like, PostDate, Posting), ...)
#
# print(str(tuple_collected_postings_instances[0][2]).split('-')[0])
# print(tuple_collected_postings_instances[10][2])
#
# print(tuple_collected_postings_instances[0][2] - tuple_collected_postings_instances[10][2])

dic = {1:'aaa', 2:'bbb'}

dic.values() = map(lambda x: x[-1],dic.values())

print(dic)