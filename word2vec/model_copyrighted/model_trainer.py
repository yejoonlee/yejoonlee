from yeznable.word2vec import functions_for_w2v

name_model = 'name_sample'
model = functions_for_w2v.Word2Vec.load('%s'%name_model)
print(model)

cursor = functions_for_w2v.cursor
cursor.execute("select column_sample from table_sample where category = 'recent'")
data_sample = cursor.fetchall()
index = 0

for datum in data_sample:

    tokenized_contents = functions_for_w2v.tokenize(datum)
    model.build_vocab(tokenized_contents, update=True)
    model.train(tokenized_contents, total_examples=model.corpus_count, epochs=model.iter)
    print(str(index)+': trained')
    index+=1

name_model_v_up = 'name_sample_v_up'
print(model)
model.save('%s'%name_model_v_up)
