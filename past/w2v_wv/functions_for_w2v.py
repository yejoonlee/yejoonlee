from nltk import regexp_tokenize

def tokenize(contents):
    pattern = "[\w']+"
    tokenized_contents = regexp_tokenize(contents, pattern)
    # filtered_sentence = [w for w in tokenized_contents if not w in stop_words]
    return tokenized_contents

