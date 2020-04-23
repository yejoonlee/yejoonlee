def load_data(csv_file, split=0.9):
    data = pd.read_csv(csv_file)

    # Shuffle data
    train_data = data.sample(frac=1, random_state=7)

    texts = train_data.text.values
    labels = [{"POSITIVE": bool(y), "NEGATIVE": not bool(y)}
              for y in train_data.sentiment.values]
    split = int(len(train_data) * split)

    train_labels = [{"cats": labels} for labels in labels[:split]]
    val_labels = [{"cats": labels} for labels in labels[split:]]

    return texts[:split], train_labels, texts[split:], val_labels


train_texts, train_labels, val_texts, val_labels = load_data('../input/nlp-course/yelp_ratings.csv')

# print('Texts from training data\n------')
# print(train_texts[:2])
# print('\nLabels from training data\n------')
# train_labels[:2]

####

import spacy

# Create an empty model
nlp = spacy.blank("en")

# Create the TextCategorizer with exclusive classes and "bow" architecture
textcat = nlp.create_pipe(
              "textcat",
              config={
                "exclusive_classes": True,
                "architecture": "bow"})

# Add the TextCategorizer to the empty model
nlp.add_pipe(textcat)

# Add labels to text classifier
textcat.add_label("NEGATIVE")
textcat.add_label("POSITIVE")

####

# from spacy.util import minibatch
# import random
#
#
# def train(model, train_data, optimizer):
#     losses = {}
#     random.seed(1)
#     random.shuffle(train_data)
#
#     batches = minibatch(train_data, size=8)
#     for batch in batches:
#         # train_data is a list of tuples [(text0, label0), (text1, label1), ...]
#         # Split batch into texts and labels
#         texts, labels = zip(*batch)
#
#         # Update model with texts and labels
#         model.update(texts, labels, sgd=optimizer, losses=losses)
#
#     return losses

####

# Fix seed for reproducibility
spacy.util.fix_random_seed(1)
random.seed(1)

optimizer = nlp.begin_training()
train_data = list(zip(train_texts, train_labels))
losses = train(nlp, train_data, optimizer)
print(losses['textcat'])

####

def predict(model, texts):
    # Use the model's tokenizer to tokenize each input text
    docs = [model.tokenizer(text) for text in texts]

    # Use textcat to get the scores for each doc
    textcat = model.get_pipe('textcat')
    scores, _ = textcat.predict(docs)

    # From the scores, find the class with the highest score/probability
    predicted_class = scores.argmax(axis=1)

    return predicted_class

####

def evaluate(model, texts, labels):
    """ Returns the accuracy of a TextCategorizer model.

        Arguments
        ---------
        model: ScaPy model with a TextCategorizer
        texts: Text samples, from load_data function
        labels: True labels, from load_data function

    """
    # Get predictions from textcat model (using your predict method)
    predicted_class = predict(model, texts)

    # From labels, get the true class as a list of integers (POSITIVE -> 1, NEGATIVE -> 0)
    true_class = [int(each['cats']['POSITIVE']) for each in labels]

    # A boolean or int array indicating correct predictions
    correct_predictions = predicted_class == true_class

    # The accuracy, number of correct predictions divided by all predictions
    accuracy = correct_predictions.mean()

    return accuracy

accuracy = evaluate(nlp, val_texts, val_labels)
print(f"Accuracy: {accuracy:.4f}")

####