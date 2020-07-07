from bs4 import BeautifulSoup
import requests
import csv
import pymysql.cursors
connection = pymysql.connect(host='117.17.250.45',
                             user='ROOT',
                             password='imlab506',
                             db='wv_db',
                             charset='utf8')
cursor = connection.cursor()

cursor.execute("select journal_title, issn from raw_data where publisher = 'elsevier'")
data = cursor.fetchall()
connection.close()

f = open("index.csv",'w')
f2 = open('journal_indexed.csv','w')
w = csv.writer(f)
w2 = csv.writer(f2)
# https://www.elsevier.com/journals/저널타이틀/ISSN/abstracting-indexing
# e.g.) https://www.elsevier.com/journals/enfermeria-clinica-english-edition/2445-1479/abstracting-indexing
for i,t in enumerate(data):
    title = t[0].lower()
    issn = t[1]
    print(title, issn)
    r = requests.get("https://www.elsevier.com/journals/%s/%s/abstracting-indexing"%(title,issn))
    soup1 = BeautifulSoup(r.text, "html.parser")
    a = soup1.find("ul", class_= "abstr-index-list")
    if a == None:
        print("None!!")
        continue
    lIndex = a.find_all("li")
    for index in lIndex:
        sIndex = index.text
        llIndex = sIndex.split('\n')
        for s in llIndex:
            # print(s)
            w.writerow([s])
    w2.writerow([issn])
    print(i)

        # sci
        # ssci
        # scie
        # Scopus

# f = open("indexed_elsevier.txt",'w')
# for i,t in enumerate(data):
#     if t[0] == None or t[0] == '':
#         continue
#     print(t[0])
#     try:
#         r = requests.get(t[0])
#     except:
#         continue
#     if "Abstracting/ Indexing" in r.text:
#         f.write(t[0]+"\n")
# f.close()