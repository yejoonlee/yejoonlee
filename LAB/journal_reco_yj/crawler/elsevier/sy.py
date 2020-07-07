import pymysql
import json
mydb = pymysql.connect(host='117.17.250.45',
                             user='ROOT',
                             password='imlab506',
                             db='wv_db',
                             charset='utf8')
cursor = mydb.cursor()

cursor.execute('select issn,subject_category from wv_db.feature')
for i in cursor.fetchall():
    one = i[1]
    if not one:
        continue
    # print(one)
    list1=one.split(',')
    # print(list1)
    out=json.dumps(list1)
    # out = json.dumps(one)
    print(out)
    print(i[0])
    cursor.execute('update wv_db.feature set subject=%s where issn =%s',(out,i[0]))

mydb.commit()