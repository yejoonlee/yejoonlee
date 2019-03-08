import pymysql.cursors
# from gensim.models import Word2Vec
import gensim
import nltk
from nltk import regexp_tokenize
from nltk.corpus import stopwords
import csv
import operator
nltk.download("stopwords")

stop_words = set(stopwords.words('english'))

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()

def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
    filtered_sentence = [w for w in tokenized_contents if not w in stop_words]
    return filtered_sentence

def cal_sim(model, lJournalTokenized, lTestTokenized):
    sim2 = 0
    exceptNum2 = 0
    lJournal = list(set(lJournalTokenized))
    lTest = list(set(lTestTokenized))
    for jToken in lJournal:
        sim1 = 0
        exceptNum = 0
        for tToken in lTest:
            try:
                sim1 += model.wv.similarity(tToken,jToken)
            except:
                exceptNum+=1
                continue
        try:
            sim2 += sim1/(len(lTest)-exceptNum)
        except:
            exceptNum2+=1
            print('division by 0')
            continue
    avg_sim = sim2 / (len(lJournal)-exceptNum2)
    return avg_sim

def sim(model, dicData, tTest):
    dicSim = {}
    # len(embedding_model.wv.index2word)
    for sJornalKey in dicData.keys():
        tokenized_data = dicData.get(sJornalKey)
        # dicSim[cal_sim(model, tokenized_data, tTest)] = sJornalKey
        dicSim[sJornalKey] = cal_sim(model, tokenized_data, tTest)
    print("calculate sim...")
    ranked_sim = sorted(dicSim.items(), key=operator.itemgetter(1), reverse=True)
    # max_sim = max(dicSim.keys())

    i = 1
    ranked_journal = {}
    for key in ranked_sim:
        if i > 5:
            break
        ranked_journal[key[0]] = dicSim.get(key[0])
        i+=1

    # return [dicSim, max_sim, dicSim.get(max_sim)]
    return [dicSim, ranked_journal, ranked_sim]







# category = 'title'
# category = 'abstract'
# category = 'keywords'
category = 'combined_text'
model = gensim.models.Word2Vec.load('%s_model(300d)_swe_v0.1'%category)
# model = gensim.models.Word2Vec.load('%s_model(300d)_v0.2'%category)


f = open("./data/ybtest.csv", "r", encoding='utf-8')
input_data = csv.reader(f)
input = {}
for line in input_data:
    if line != []:
        input['test'] = tokenize(line[0])
input_keys = input.keys()

journals = []
journal_text = {}
cursor.execute("select * from representative_document where category = 'recent'")
documents = cursor.fetchall()
for document in documents:
    if document[-4] in journals:
        journal_text[document[-4]].append(document[2]+" "+document[3]+" "+document[4])
    else:
        journal_text[document[-4]] = [document[2]+" "+document[3]+" "+document[4]]
print("made journal_text")

journal_token = {}
for journal in journal_text.keys():
    combined_text = " ".join(journal_text[journal])
    tokenized_text = tokenize(combined_text)
    journal_token[journal] = tokenized_text
# journal_keys = journal_token.keys()
print("made journal_token")

for input_token in input.values():
    result = sim(model,journal_token,input_token)
    lResult = result[1]

for recoJ in lResult:
    cursor.execute("select * from feature where title = '%s'" % recoJ)
    feature = cursor.fetchone()
    print(recoJ)
    try:
        print("     Subject : "+feature[-2])
    except:
        print("     Subject : ")
    try:
        print("     Impact factor : "+feature[25])
    except:
        print("     Impact factor : ")
