# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import pickle

# 분석할 텍스트파일의 이름들을 lFileName 리스트에 담고 그 안의 텍스트를 \n으로 나누어 contents 리스트에 담는다.
# 즉, 파일에 들어있는 텍스트의 한줄 한줄이 하나의 문서로 구분된다.
def create_tf(lFileName, spliter):

    contents = []
    for fileName in lFileName:
        file = open("./data/%s.txt"%fileName,'r')
        text = file.read()
        text = text.split("\n")
        contents+=text
        file.close()

    # 분석에서 제외할 단어를 stop_words 리스트에 담아둔다.
    # contents 리스트에 담긴 각 문서들을 stop_words에 속한 형태소들은 제거하여 input 리스트에 담고 lNouns 리스트에는 형태소들을 모두 담는다.
    # 모델을 학습할 입력 데이터가 완성되었다는 알림을 한다.
    input = []
    lNouns = []
    stop_words = ['word1','word2']
    for line in contents:
        nouns = spliter.nouns(line)
        # check
        nouns_stoped = [i for i in nouns if i not in stop_words]
        input.append(" ".join(nouns_stoped))
        lNouns += nouns

    # lNouns에 중복된 요소들을 제거하고 길이를 받아 모델의 파라미터중 하나인 no_features를 찾는다.
    # no_features를 알려준다.
    # 토픽에 속한 features중 보고싶은 상위 유사도를 갖는 단어 개수를 지정한다.
    len_words = len(set(lNouns))
    no_features = int(len_words)
    print(no_features)

    # CountVectorizer를 원하는 파라미터로 생성하여 tf_vectorizer로 정의
    # tf_vectorizer에 아까 만든 input를 fit_transform함수로 입력
    # input이 입력된 tf_vectorizer에서 get_feature_names함수로 피쳐들을 받아 tf_feature_names로 정의
    # 토픽의 수를 topic_num으로 정의
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=1, max_features=no_features, stop_words=stop_words)
    tf = tf_vectorizer.fit_transform(input)
    tf_feature_names = tf_vectorizer.get_feature_names()

    print("Input is made")

    return [tf, tf_feature_names]

# 원하는 모델의 형태를 만들어 pickle 패키지의 dump 함수로 저장
def save_LDA_model(tf_feature_names,lda,topic_num):
    model = (tf_feature_names, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_)
    with open('./results/' + "topic%d_model" % topic_num, 'wb') as fp:
        # check
        pickle.dump(model, fp)
    return

def display_features(topic_num, model, feature_names, no_top_words):

    f_t = open("./results/topics_%d.csv" % topic_num, 'w')
    wr = csv.writer(f_t)
    wr.writerow(["no_topic = %d" % topic_num])
    print("no_topic = %d" % topic_num)

    for features_idx, features in enumerate(model.components_):
        print("Topic %d" % (features))
        f_t.writerow(["Topic %d:" % (features)])
        # check
        lfeatures = features.argsort()[:-(no_top_words + 1):-1]
        for i in lfeatures:
            f_t.writerow([str(feature_names[i]),str(features[i])])

    f_t.close()
    print("Complete")

def calulate_perplexity(tf,lda):
    gamma = lda.transform(tf)
    perplexity = lda.perplexity(tf, gamma)
    return perplexity