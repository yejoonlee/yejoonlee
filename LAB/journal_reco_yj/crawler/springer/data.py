import csv
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()


cursor.execute("select articles_num from html where publisher = 'mdpi'")
data = cursor.fetchall()

f = open('data.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
for a in data:
    a=str(a)
    a = a[2:-3]
    a = a.replace(",","")
    wr.writerow([a])
f.close()