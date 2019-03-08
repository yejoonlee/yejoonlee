import pymysql.cursors
from gensim.models import Word2Vec
import gensim
#import nltk
from nltk import regexp_tokenize
from nltk.corpus import stopwords
#nltk.download("stopwords")

#stop_words = set(stopwords.words('english'))
import csv

def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
#    filtered_sentence = [w for w in tokenized_contents if not w in stop_words]
    return tokenized_contents

# category = 'title'
# category = 'abstract'
# category = 'keywords'
category = 'combined_text'

#0.2: ~1000
#0.3: ~10000
#0.4: ~20000
#0.5: ~40000
#0.6: ~end


#(300d)_v0.1: ~40000
model = gensim.models.Word2Vec.load('%s_model(700d)'%category)
print(model)

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8'
                             )
cursor = connection.cursor()

#지금은 엘스비어의 recent에서 학습
cursor.execute("select distinct(title) from representative_document where category = 'recent'")
lTitle = cursor.fetchall()

range_before = -1
range = 80000
index = 0

# f1 = open('learned_title.csv', 'r', encoding='utf-8')
# learned_titles = list(csv.reader(f1))
# print(learned_titles)


for title in lTitle:
    if index <= range_before:
        index+=1
        continue
    if index > range:
        break
    # if title[0] in learned_titles:
    #     print("already learned...")
    #     continue
    if category == 'combined_text':
        cursor.execute("select * from representative_document where title = '%s'"%title)
        contents = cursor.fetchone()
        tTitle = tokenize(title[0])
        try:
            tAbstract = tokenize(contents[2])
            tKeywords = tokenize(contents[4])
            tContents = [tTitle,tAbstract,tKeywords]
        except:
            index+=1
            continue
        model.build_vocab(tContents, update=True)
        model.train(tContents,total_examples=model.corpus_count, epochs=model.iter)
        print(str(index)+': training %s...'%category)
    else:
        cursor.execute("select %s from representative_document where category = 'recent'"%category)
        contents = cursor.fetchone()
        try:
            tContents = tokenize(contents[0])
        except:
            index += 1
            continue
        model.build_vocab(tContents, update=True)
        model.train(tContents,total_examples=model.corpus_count, epochs=model.iter)
        print(str(index)+': training %s...'%category)
    # learned_titles.append(title[0])
    index+=1

# print(learned_titles)
print(model)
model.save('%s_model(700d)_v0.1'%category)

# f2 = open('learned_title.csv', 'w', encoding='utf-8')
# wr = csv.writer(f2)
# wr.writerow(learned_titles)
# f1.close()
# f2.close()