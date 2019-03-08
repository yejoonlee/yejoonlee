from yeznable.word2vec import functions_for_w2v

name_model = 'name_sample'

text_sample = "sample sample sample sample sample"

tokenized_sample = functions_for_w2v.tokenize(text_sample)
print(tokenized_sample)

model = functions_for_w2v.Word2Vec(tokenized_sample, size=700, window = 5, min_count=1, workers=4, iter=100, sg=0)

model.save('%s'%name_model)

# model = gensim.models.Word2Vec.load('keywords_model')
# print(model)