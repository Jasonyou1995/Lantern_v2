"""
Returns the top n words in the given dictionary that most matches the unknown word"""

import os
from gensim.models import word2vec


# this:          returns a list with n tuples of (similar_word, cos_similarity) pairs
# unknown_word:  word that is not in the dictionary
# dictionary:    one of the dictionaries from C1-C8
# top_n:         choose top N similar words
# model:         model from the load_model() method
def cos_max_word(unknown_word, dictionary, top_n, model):
    similarity = dict()

    for word in dictionary:
        cos_similarity = model.similarity(word, unknown_word)
        similarity.update({word: cos_similarity})

    # sorts the cos similarity in decreasing order
    ordered_words = sorted(similarity.items(), key=lambda x: x[1], reverse=True)
    return ordered_words[:top_n]


# this:          returns a word2vec model
# model_path:    path to the text.model.bin file
def load_model(model_path):
    return word2vec.Word2Vec.load_word2vec_format(model_path, binary=True)


def main():
    print(os.getcwd())

    unk = 'violence'
    d1 = ['good', 'bad', 'life', 'cheat', 'school', 'the', 'a', 'crime', 'conflict']

    my_model = load_model('text.model.bin')     # load the word2vec model
    print(cos_max_word(unk, d1, 3, my_model))   # print the most similar word(s)

if __name__ == '__main__':
    main()
