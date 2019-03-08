import gensim
from nltk import regexp_tokenize

def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
    return tokenized_contents

title = "How could stress lead to major depressive disorder?"
abstract = "Stress is associated with major depressive disorder (MDD), but the underlying mechanism remains elusive. However, some experiences, referred to as stress, may actually lead to resilience. It is thus critical first to define what type of stress may lead to MDD. Long-term potentiation (LTP) and long-term depression (LTD) are both sensitive to stress, but particularly to inescapable and not escapable stress. Thus, these are the psychological aspects of stress which contribute to the development of MDD, but by which mechanisms remains still elusive. Interestingly, the same stress may facilitate LTD and impair LTP in the CA1 region. In addition, repeated efforts are often required for learning under neutral conditions but single- or few learning trials are sufficient for forming stress-related memories. If LTP is crucial for normal learning, a combination of limited LTP and facilitated LTD appears to have higher efficiency for storing stress-related memories. Chronic psychological stress may cause a hyper-link among stress-related memories across the spatiotemporal due to shared quality of inescapability, leading to automatically negative appraisal through memory generalization mechanisms in MDD patients when encountering new distinct events which are perceived to share such similarity with previous experiences."
keywords = "Major depressive disorder Stress Memory"

tTitle = tokenize(title)
tAbstract = tokenize(abstract)
tKeywords = tokenize(keywords)
tCombined_text = [tTitle,tAbstract,tKeywords]
print(tCombined_text)

# title_model = gensim.models.Word2Vec(tTitle, size=100, window = 5, min_count=1, workers=4, iter=100, sg=0)
# abstract_model = gensim.models.Word2Vec(tAbstract, size=100, window = 5, min_count=1, workers=4, iter=100, sg=0)
# keywords_model = gensim.models.Word2Vec(tKeywords, size=100, window = 5, min_count=1, workers=4, iter=100, sg=0)
combined_text_model = gensim.models.Word2Vec(tCombined_text, size=700, window = 5, min_count=1, workers=4, iter=100, sg=0)
#
# # print(abstract_model)
# title_model.save('title_model')
# abstract_model.save('abstract_model')
# keywords_model.save('keywords_model')
combined_text_model.save('combined_text_model(700d)')

# model = gensim.models.Word2Vec.load('keywords_model')
# print(model)