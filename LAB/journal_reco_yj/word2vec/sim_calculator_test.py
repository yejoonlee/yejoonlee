import pymysql.cursors
# from gensim.models import Word2Vec
import gensim
import nltk
from nltk import regexp_tokenize
# from nltk.corpus import stopwords
import csv
import operator
# nltk.download("stopwords")
#
# stop_words = set(stopwords.words('english'))

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()


def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
    # filtered_sentence = [w for w in tokenized_contents if not w in stop_words]
    return tokenized_contents

def cal_sim(model, lJournalTokenized, lTestTokenized):
    sim2 = 0
    exceptNum2 = 0
    lJournal = list(set(lJournalTokenized))
    lTest = list(set(lTestTokenized))
    for jToken in lJournal:
        sim1 = 0
        exceptNum1 = 0
        for tToken in lTest:
            try:
                sim1 += model.wv.similarity(tToken, jToken)
            except:
                exceptNum1 += 1
                continue
        try:
            sim2 += sim1 / (len(lTest) - exceptNum1)
        except:
            exceptNum2+=1
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

    # i = 1
    ranked_journal = {}
    for key in ranked_sim:
        ranked_journal[key[0]] = dicSim.get(key[0])
        # i += 1

    # return [dicSim, max_sim, dicSim.get(max_sim)]
    return [dicSim, ranked_journal, ranked_sim]

def sco(ranked_journal, k):
    rank = 0
    score = 0
    for key in ranked_journal:
        if k.upper() == key:
            rank += 1
            score = rank/len(ranked_journal)
            print(score)
            break
        rank += 1

    # scoreSum = 0
    # for s in scores:
    #     scoreSum += s
    # accuracy = scoreSum / 5

    return score



# category = 'title'
# category = 'abstract'
# category = 'keywords' regedit
category = 'combined_text'
model = gensim.models.Word2Vec.load('%s_model(700d)_v0.1' % category)

# f = open("./data/test_input_elsevier.csv", "r", encoding='utf-8')
f = open("test1.csv", "r", encoding='utf-8')
input_data = csv.reader(f)
input = {}
for line in input_data:
    # text = str(line[0])
    # if len(text) < 150:
    #     continue
    if line != []:
        input[line[1]] = tokenize(line[0])
        # input[tokenize(line[0])] = line[1]
input_keys = input.keys()

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

lResult = []
for input_token in input.values():
    result = sim(model, journal_token, input_token)
    lResult.append(result)

lScore = []
resultIndex = 0
for k in input.keys():
    thisResult = lResult[resultIndex]
    score = sco(thisResult[1].keys(), k)
    lScore.append(score)
    resultIndex+=1
# print(lTopTitles)

scoreSum = 0
for s in lScore:
    scoreSum += s
accuracy = scoreSum / len(lScore)

print(lScore)
print(accuracy)
