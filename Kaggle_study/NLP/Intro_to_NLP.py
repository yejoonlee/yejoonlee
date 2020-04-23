# import spacy
# from spacy.matcher import PhraseMatcher
#
# index_of_review_to_test_on = 14
# text_to_test_on = data.text.iloc[index_of_review_to_test_on]
#
# # Load the SpaCy model
# nlp = spacy.blank('en')
#
# # Create the tokenized version of text_to_test_on
# review_doc = nlp(text_to_test_on)
#
# # Create the PhraseMatcher object. The tokenizer is the first argument. Use attr = 'LOWER' to make consistent capitalization
# matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
#
# # Create a list of tokens for each item in the menu
# menu_tokens_list = [nlp(item) for item in menu]
#
# # Add the item patterns to the matcher.
# # Look at https://spacy.io/api/phrasematcher#add in the docs for help with this step
# # Then uncomment the lines below
#
#
# matcher.add("MENU",            # Just a name for the set of rules we're matching to
#            None,              # Special actions to take on matched words
#            *menu_tokens_list
#           )
#
# # Find matches in the review_doc
# matches = matcher(review_doc)


#

# from collections import defaultdict
#
# # item_ratings is a dictionary of lists. If a key doesn't exist in item_ratings,
# # the key is added with an empty list as the value.
# item_ratings = defaultdict(list)
#
# for idx, review in data.iterrows():
#     doc = nlp(review.text)
#     # Using the matcher from the previous exercise
#     matches = matcher(doc)
#
#     # Create a set of the items found in the review text
#     found_items = set([doc[match[1]:match[2]] for match in matches])
#
#     # Update item_ratings with rating for each item in found_items
#     # Transform the item strings to lowercase to make it case insensitive
#     for item in found_items:
#         item_ratings[str(item).lower()].append(review.stars)

#

# # Calculate the mean ratings for each menu item as a dictionary
# mean_ratings = {item: sum(ratings)/len(ratings) for item, ratings in item_ratings.items()}
#
# # Find the worst item, and write it as a string in worst_text. This can be multiple lines of code if you want.
# worst_item = sorted(mean_ratings, key=mean_ratings.get)[0]
#
# #
#
# counts = {item: len(ratings) for item, ratings in item_ratings.items()}
#
# item_counts = sorted(counts, key=counts.get, reverse=True)
# for item in item_counts:
#     print(f"{item:>25}{counts[item]:>5}")
#
# #
#
# sorted_ratings = sorted(mean_ratings, key=mean_ratings.get)
#
# print("Worst rated menu items:")
# for item in sorted_ratings[:10]:
#     print(f"{item:20} Ave rating: {mean_ratings[item]:.2f} \tcount: {counts[item]}")
#
# print("\n\nBest rated menu items:")
# for item in sorted_ratings[-10:]:
#     print(f"{item:20} Ave rating: {mean_ratings[item]:.2f} \tcount: {counts[item]}")