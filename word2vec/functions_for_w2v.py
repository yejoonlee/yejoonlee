import pymysql.cursors
from gensim.models import Word2Vec
from nltk import regexp_tokenize
import operator

connection = pymysql.connect(host='myhost',
                             user='myuser',
                             password='mypassword',
                             db='mydb',
                             charset='charset'
                             )
cursor = connection.cursor()

# contents : NLP
def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
    # filtered_sentence = [w for w in tokenized_contents if not w in stop_words]
    return tokenized_contents

# lDocuments_learned    : list [[tokenized_document],[tokenized_document],[tokenized_document]]
# lDocuments_new        : list [[tokenized_document],[tokenized_document],[tokenized_document]]
def calculate_similarity(model, lDocuments_learned, lDocuments_new):
    similarity_max_sum = 0
    for token_new in lDocuments_new:
        similarity = []
        for token_learned in lDocuments_learned:
            try:
                similarity.append(model.wv.similarity(token_new, token_learned))
            except:
                continue
        try:
            similarity_max_sum += max(similarity)
        except:
            continue
    similarity_average = similarity_max_sum / len(lDocuments_new)
    return similarity_average

# model             : word2vec model
# dicData           : dictionary
# lDocuments_new    : list [[tokenized_document],[tokenized_document],[tokenized_document]]
def rank_similarity(model, dicData, lDocuments_new):
    dicSimilarity = {}
    print("Calculating similarity...")
    for sKey in dicData.keys():
        lDocuments_learned = dicData.get(sKey)
        dicSimilarity[sKey] = calculate_similarity(model, lDocuments_learned, lDocuments_new)
    ranked_similarity = sorted(dicSimilarity.items(), key=operator.itemgetter(1), reverse=True)

    number_top = 5
    index = 1
    ranked_document = {}
    for lKey in ranked_similarity:
        if index > number_top:
            break
        ranked_document[lKey[0]] = dicSimilarity.get(lKey[0])
        index+=1

    print("Calculate completely")
    return [ranked_document, ranked_similarity]

def score(ranked_document, sKey):
    value = 0
    for rank,document_key in enumerate(ranked_document):
        if sKey.upper() == document_key.upper():
            value = rank/len(ranked_document)
            print(value)
            break

    # scoreSum = 0
    # for s in scores:
    #     scoreSum += s
    # accuracy = scoreSum / 5

    return value