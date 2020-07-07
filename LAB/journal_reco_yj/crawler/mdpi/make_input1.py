import csv
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()

cursor.execute("select * from representative_document where idx > 20000")
representative_documents = cursor.fetchall()

i = 1
jTitleBefore = ""
lTitle = []
lAbstract = []
lKeywords = []
lAll = []

f = open('datainput.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
index = ['title', 'abstract', 'keywords', 'all', 'subject']
wr.writerow(index)
for representative_document in  representative_documents:
    #if i > 2:
    #    break
    jTitle = representative_document[-2]
    if jTitle != jTitleBefore:
        subject = jTitleBefore
        sTitle = " ".join(lTitle)
        sAbstract = " ".join(lAbstract)
        sKeywords = " ".join(lKeywords)
        lAll.append(sTitle)
        lAll.append(sAbstract)
        lAll.append(sKeywords)
        sAll = " ".join(lAll)
        lAll.append(sAll)
        lAll.append(subject)
        wr.writerow(lAll)
        lTitle = []
        lAbstract = []

        lKeywords = []
        lAll = []
        jTitleBefore = representative_document[-2]
        print(i)
        i+=1
        continue
    jTitleBefore = representative_document[-2]
    lTitle.append(representative_document[3])
    lAbstract.append(representative_document[4])
    lKeywords.append(representative_document[5])
    print(i)
    i+=1
f.close()