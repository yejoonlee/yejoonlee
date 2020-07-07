from bs4 import BeautifulSoup
import requests
import pymysql.cursors
connection = pymysql.connect(host='117.17.250.45',
                             user='ROOT',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()

cursor.execute("select main_url, journal_title, issn from raw_data where publisher = 'elsevier'")
lJournal = cursor.fetchall()

for i,journal in enumerate(lJournal):
    print(i)
    if i < 88:
        continue
    issn = journal[2]
    journal_title = journal[1]
    r = requests.get(journal[0])

    soup1 = BeautifulSoup(r.text, "html.parser")
    AnS = soup1.find("div", class_= "full-scope")
    if AnS == None:
        continue
    try:
        AnS = AnS.find("p").text
    except:
        continue
    title = journal_title+"_Aims&Scope"
    abstract = AnS

    cursor.execute("insert into representative_document_0609 (title, abstract, journal_title,issn) values('%s','%s','%s','%s')"%(title.replace("'","^"), abstract.replace("'","^"), journal_title.replace("'","^"),issn))
    print("insert %s"%journal_title)
    connection.commit()
connection.close()