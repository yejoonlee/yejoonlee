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
    s_sim = 0
    lJournal = list(set(lJournalTokenized))
    lTest = list(set(lTestTokenized))
    for jToken in lTest:
        sim = []
        for tToken in lJournal:
            try:
                sim.append(model.wv.similarity(tToken, jToken))
            except:
                continue
        try:
            s_sim += max(sim)
        except:
            continue
    avg_sim = s_sim / len(lTest)
    return avg_sim


def sim(model, dicData, lTest):
    dicSim = {}
    # len(embedding_model.wv.index2word)
    for sJornalKey in dicData.keys():
        j_d = dicData.get(sJornalKey)

        js = j_d[0].replace(" ","")
        ts = lTest[0].replace(" ","")
        js = js.split(",")
        ts = ts.split(",")
        i = 0
        for s in js:
            for ss in ts:
                if s == ss:
                    i = 0
                    break
                else:
                    i+=1
            if i == 0:
                break
        # dicSim[cal_sim(model, tokenized_data, tTest)] = sJornalKey
        if i != 0:
            continue
        dicSim[sJornalKey] = cal_sim(model, j_d[1], lTest[1])
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
    score = 0
    for rank,key in enumerate(ranked_journal):
        if k.upper() == key:
            score = rank/len(ranked_journal)
            print(score)
            break

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
input = {}
f = open("test_with_subject.csv", "r", encoding='utf-8')
input_data = csv.reader(f)
for line in input_data:
    # text = str(line[2])
    # if len(text) < 150:
    #     continue
    if line == []:
        continue
    input[line[0]] = [line[1],tokenize(line[2])]
    # input[tokenize(line[0])] = line[1]
input_keys = input.keys()
print("load test data")
f.close()

journal = {}
f = open("data/journal_token.csv",'r')
journal_data = csv.reader(f)
for line in journal_data:
    if line == []:
        continue
    journal[line[0]] = [line[1],line[2]]
print("load journal data")

# journal_token = {}
# for journal in journal_text.keys():
#     combined_text = " ".join(journal_text[journal])
#     tokenized_text = tokenize(combined_text)
#     journal_token[journal] = tokenized_text
# # journal_keys = journal_token.keys()
# print("made journal_token")

lResult = []
for input_value in input.values():
    result = sim(model, journal, input_value)
    lResult.append(result)

lScore = []
for i,k in enumerate(input.keys()):
    thisResult = lResult[i]
    score = sco(thisResult[1].keys(), k)
    lScore.append(score)
# print(lTopTitles)

scoreSum = 0
for s in lScore:
    scoreSum += s
accuracy = scoreSum / len(lScore)

print(lScore)
print(accuracy)