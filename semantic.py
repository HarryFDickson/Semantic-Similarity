import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("orange")
word2 = nlp("tangerine")
word3 = nlp("green")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("\n---------[Separator]---------\n")

tokens = nlp('orange tangerine green hello')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\n---------[Separator]---------\n")

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# -------Bullet Point 2-------
# What I have found interesting about the similarities between cat, monkey and banana is the fact that cat and monkey are both animals, so in a way they are the most similar, whereas when monkey and banana are compared, they are somewhat similar because the monkey eats bananas. But if you were to compare cats and bananas, they are barely similar because cats are not likely to eat bananas.

# -------Bullet Point 3-------
# The main difference between the two models 'en_core_web_md' and 'en_core_web_sm' in the spacy library is their size and performance.

# 'en_core_web_sm' is a smaller model that is trained on a small dataset and includes only essential linguistic annotations such as part-of-speech tags, dependency parsing, and named entity recognition. This model is suitable for simple text analysis tasks and is faster to load and use.

# On the other hand, 'en_core_web_md' is a medium-sized model that is trained on a larger dataset and includes additional features such as word vectors and syntax. This model is more accurate and performs better on complex text analysis tasks but is slower to load and use compared to the smaller model.

# In summary, if you need a faster and lightweight model for basic text analysis tasks, 'en_core_web_sm' is a good choice. If you need more accurate results and are working on more complex text analysis tasks, 'en_core_web_md' is a better option.
