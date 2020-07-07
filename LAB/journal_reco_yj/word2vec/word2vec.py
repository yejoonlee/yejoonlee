# import pandas as pd
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# from sklearn.manifold import TSNE
# import matplotlib as mpl
from bs4 import BeautifulSoup
import pymysql.cursors
from gensim.models import Word2Vec
import gensim
from nltk import regexp_tokenize
import csv
#f1 = open('datainput2.csv', 'r', encoding='ISO-8859-1')
#training_data = csv.reader(f1)
f2 = open('test_input_elsevier.csv', 'r', encoding='ISO-8859-1')
test_data = csv.reader(f2)

#def get_data(index, document1, document2): #index = 0:tite, 1:abstract, 2:keywords, 3:all //4:subject(journal title)
#    i = 0
#    i2 = 1
#    dicData = {}
#    for line in document1:
#        # print(line)
#        if i == 0:
#            i+=1
#            continue
#        # if i > 2:
#        #     break
#        try:
#            dicData[line[4]] = line[index] # dic = {subject:journal_data}
#        except:
#             continue
#     for line in document2:
#         if i2 == 1: # i2 = 1~5 ekdmadp 2
#             sTest = line[index]
#             break
#         else:
#             i2+=1
#             continue
#
#     embedding_contents = " ".join(dicData.values()) + " " + sTest
#     # print(dicData)
#     # print(embedding_contents)
#     return [embedding_contents, dicData, sTest]

def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
    return tokenized_contents

def cal_sim(model, lJournalTokenized, lTestTokenized):
    sim = 0
    lJournal = list(set(lJournalTokenized))
    lTest = list(set(lTestTokenized))
    exceptNum = 0
    for jToken in lJournal:
        for tToken in lTest:
            try:
                sim += model.wv.similarity(tToken,jToken)
            except:
                exceptNum+=1
                continue
    avg_sim = (sim/len(lJournal))/(len(lTest)-exceptNum)
    return avg_sim

def sim(embedding_model, dicData, tTest):
    dicSim = {}
    # len(embedding_model.wv.index2word)
    for sJornalKey in dicData.keys():
        data_list = dicData.get(sJornalKey)
        tokenized_data =tokenize(" ".join(data_list))
        dicSim[cal_sim(embedding_model, tokenized_data, tTest)] = sJornalKey
    ranked_sim = sorted(dicSim.keys(),reverse=1)
    # max_sim = max(dicSim.keys())
    i = 0
    ranked_journal = {}
    for key in ranked_sim:
        if i > 4:
            break
        ranked_journal[key] = dicSim.get(key)
        i+=1

    # return [dicSim, max_sim, dicSim.get(max_sim)]
    return [dicSim, ranked_journal, ranked_sim]








connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()

cursor.execute("select distinct(title) from representative_document where category ='recent'")
titles_list = cursor.fetchall()

dicTitle = {}
dicAbstract = {}
# dicKeywords = {}
lJournal = []

i = 1
for title in titles_list:
    # if i>50:
    #     break
    sTitle = title[0]
    cursor.execute("select * from representative_document where title = '%s'" % sTitle)
    row = cursor.fetchone()

    print(str(i)+" : Data load...")
    i+=1
    sAbstract = row[2]
    # sKeywords = row[4]
    journal_title = row[-4]

    # print(sTitle, sAbstract, sKeywords, journal_title)
    if journal_title in lJournal:
        dicTitle[journal_title].append(sTitle)
        dicAbstract[journal_title].append(sAbstract)
        # dicKeywords[journal_title].append(sKeywords)
    else:
        dicTitle[journal_title] = [sTitle]
        dicAbstract[journal_title] = [sAbstract]
        # dicKeywords[journal_title] = [sKeywords]
        lJournal.append(journal_title)
# print(dicTitle)
# print(dicAbstract)
print("Data loaded!")

dicTitle_token = {}
dicAbstract_token = {}
# dicKeywords_token = {}
for journal in lJournal:
#    data = get_data(3,training_data, test_data) #index = 0:tite, 1:abstract, 2:keywords, 3:all //4:subject(journal title)
    title_token = []
    abstract_token = []
    # keywords_token = []
    for title in dicTitle[journal]:
        title_token.append(tokenize(title))
    for abstract in dicAbstract[journal_title]:
        abstract_token.append(tokenize(abstract))
    # for keywords in dicKeywords[journal]:
    #     keywords_token.append(tokenize(keywords))
    # print(title_token)
    dicTitle_token[journal] = title_token
    dicAbstract_token[journal] = abstract_token
    # dicKeywords_token[journal] = keywords_token
print("Data tokenized...")

embedding_title = list(dicTitle_token.values())
embedding_title = [row_element for row in embedding_title for row_element in row]
# embedding_title = [element for sub_matrix in embedding_title for sub_matrix_list in sub_matrix for element in sub_matrix_list]
print(embedding_title)
embedding_abstract = list(dicAbstract_token.values())
embedding_abstract = [row_element for row in embedding_abstract for row_element in row]
print(embedding_abstract)
# embedding_keywords = list(dicKeywords_token.values())
# embedding_keywords = [row_element for row in embedding_keywords for row_element in row]

title_model = gensim.models.Word2Vec(embedding_title, size=100, window = 5, min_count=1, workers=4, iter=100, sg=0)
abstract_model = gensim.models.Word2Vec(embedding_abstract, size=100, window = 5, min_count=1, workers=4, iter=100, sg=0)
# keywords_model = gensim.models.Word2Vec(embedding_keywords, size=100, window = 5, min_count=1, workers=4, iter=100, sg=0)

print("Complete embedding...")















a = 1
for line in test_data:
    print(line[4])
    try:
        print("test : %d" % a)
        sTest_title = line[0]
        sTest_abstract = line[1]
        sTest_keywords = line[2]
    except:
        a+=1
        continue
    a+=1
    title_sim = sim(title_model,dicTitle,sTest_title)
    abstract_sim = sim(abstract_model,dicAbstract,sTest_abstract)
    # keywords_sim = sim(keywords_model,dicKeywords,sTest_keywords)
    print("Complete training...")
    title_top = list(title_sim[1].values())
    abstract_top = list(abstract_sim[1].values())
    # keywords_top = list(keywords_sim[1].values())
    print("title_top : "+str(title_top))
    print("abstract_top : "+abstract_top)
    # print("keywords_top : "+keywords_top)

# 이 아래는 시각화

# mpl.rcParams['axes.unicode_minus'] = False
# vocab = list(embedding_model.wv.vocab)
# X = embedding_model[vocab]
#
# print(len(X))
# print(X[0][:10])
# tsne = TSNE(n_components=2)
#
# X_tsne = tsne.fit_transform(X[:100,:])
# df = pd.DataFrame(X_tsne, index=vocab[:100], columns=['x', 'y'])
#
# fig = plt.figure()
# fig.set_size_inches(40, 20)
# ax = fig.add_subplot(1, 1, 1)
#
# ax.scatter(df['x'], df['y'])
#
# for word, pos in df.iterrows():
#     ax.annotate(word, pos, fontsize=30)
# plt.show()