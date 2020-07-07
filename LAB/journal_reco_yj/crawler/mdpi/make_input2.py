import requests
from bs4 import BeautifulSoup
import csv
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()

cursor.execute("select distinct(title) from representative_document where publisher ='elsevier'")
titles_list = cursor.fetchall()

i = 1

f = open('datainput(elsevier).csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
index = ['title', 'abstract', 'keywords', 'all', 'journal_title']
wr.writerow(index)
for title in titles_list:
    sTitle = title[0]
    lAll = []
    print(i)
    i+=1
    cursor.execute("select * from representative_document where title = '%s'"%sTitle)
    row = cursor.fetchone()
    print(row)
    if i > 1:
        break

    journal_title = row[-4]
    sTitle = row[3]
    sAbstract = row[2]
    sKeywords = row[4]
    lAll.append(sTitle)
    lAll.append(sAbstract)
    lAll.append(sKeywords)
    lAll.append(" ".join(lAll))
    lAll.append(journal_title)
    wr.writerow(lAll)

f.close()
connection.close()