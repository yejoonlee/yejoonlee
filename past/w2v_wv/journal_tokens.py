import csv
import pymysql.cursors
from nltk import regexp_tokenize
# from nltk.corpus import stopwords

connection = pymysql.connect(host='117.17.250.45',
                             user='ROOT',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()

def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
    # filtered_sentence = [w for w in tokenized_contents if not w in stop_words]
    return tokenized_contents

journals = []
journal_text = {}
cursor.execute("select * from representative_document where category = 'recent'")
documents = cursor.fetchall()
for document in documents:
    if document[-4] in journals:
        journal_text[document[-4]].append(document[2] + " " + document[3] + " " + document[4])
    else:
        journal_text[document[-4]] = [document[2] + " " + document[3] + " " + document[4]]
print("made journal_text")

journal_token = {}
for journal in journal_text.keys():
    combined_text = " ".join(journal_text[journal])
    tokenized_text = tokenize(combined_text)
    journal_token[journal] = tokenized_text
# journal_keys = journal_token.keys()
print("made journal_token")

f = open("data/journal_token.csv", 'w')
wr = csv.writer(f)
for item in journal_token.items():
    cursor.execute("select subject_category from feature where title = '%s'"%item[0])
    subject = cursor.fetchone()
    # print(subject[0])
    wr.writerow([item[0],subject[0],item[1]])
    # wr.writerow(item[1])
f.close()