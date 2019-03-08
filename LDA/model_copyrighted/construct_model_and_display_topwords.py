# -*- coding: utf-8 -*-
from sklearn.decomposition import LatentDirichletAllocation
from konlpy import tag
# from LDA.stopwords import get_my_stop_words
import time

from yeznable.LDA import functions_for_LDA

# 모델 학습에 시간이 얼마나 걸리는지 체크하기위해 시작시간을 정의
# Define start_time for check how long to learning
start_time = time.time()
# 한국어 형태소 분석기를 지정
spliter = tag.Mecab()
no_top_words = 100
############ 토픽 수 정해주는거 찾아보기
topic_num = 5

# 분석할 텍스트파일의 이름들을 lFileName 리스트에 담고 그 안의 텍스트를 \n으로 나누어 contents 리스트에 담는다.
# 즉, 파일에 들어있는 텍스트의 한줄 한줄이 하나의 문서로 구분된다.
lFileName = ["example1","example2"]
lInputs = functions_for_LDA.create_tf(lFileName, spliter)
tf = lInputs[0]
tf_feature_names = lInputs[1]

# input을 입력받은 tf_vectorizer인 tf를
# 원하는 파라미터들로 생성된 LatentDirichletAllocation에 입력하여 lda로 정의
lda = LatentDirichletAllocation(n_topics=topic_num, max_iter=5, learning_method='online',
                            learning_offset=50., random_state=0).fit(tf)

# 원하는 모델의 형태를 만들어 pickle 패키지의 dump 함수로 저장
functions_for_LDA.save_LDA_model(tf_feature_names,lda,topic_num)
functions_for_LDA.display_features(topic_num, lda, tf_feature_names, no_top_words)

end_time = time.time()
print("Spended time: "+str(end_time - start_time))