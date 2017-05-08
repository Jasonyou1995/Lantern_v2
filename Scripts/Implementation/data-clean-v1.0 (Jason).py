
# coding: utf-8

# In[197]:

get_ipython().system('jupyter nbconvert --to script "data-clean-v1.0-Jason".ipynb')


# In[190]:

# Import packages and read from ./data repo
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
corpus_root = 'data'
wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')
ids = wordlists.fileids()

# use three documents as samples
d1 = wordlists.words(ids[0])
d2 = wordlists.words(ids[1])
d3 = wordlists.words(ids[2])

print(stopwords.readme())


# In[29]:

# Get the frequency distribution for each document
fd1 = nltk.FreqDist(d1)
fd2 = nltk.FreqDist(d2)
fd3 = nltk.FreqDist(d3)

# the words that only shown once
print(
    len(fd1.hapaxes()),
    len(fd2.hapaxes()),
    len(fd3.hapaxes()))


# In[192]:

# most common words before cleaning
print(fd1.most_common(10))
print(fd2.most_common(10))
print(fd3.most_common(10))


# In[ ]:

my_stopwords = set(['the', 'a', '.'])  # we can define our own stop words in here


# In[176]:

# Returns a set of word-frequency pairs chosen based on given limitations
# param@words: list of words from input documents
# param@freq: frequency distributions for each word from words
# param@min_len: the minimum length of a word to be chosen
# param@min_freq: the minimum times a word appear in the doc
def feature_extractor(words, freq, min_len, min_freq, my_stop=set()):
    return(set([(w.lower(), freq.get(w))
           for w in set(words)
           if len(w) >= min_len
           and freq.get(w) >= min_freq
           and w not in stopwords.words(fileids='english')
           and w not in my_stopwords]))
    # I want to add a filter to check whether the 'w' is a English word (with Lexical data)

def print_size(feature, id):
    print(' '.join(['Choosen', str(len(feature)), 'words from document', str(id)]))

# The numerical parameters in here can be tuned
f1 = feature_extractor(d1, fd1, 7, 7, my_stopwords)
f2 = feature_extractor(d2, fd2, 7, 7, my_stopwords)
f3 = feature_extractor(d3, fd3, 7, 7, my_stopwords)

print_size(f1, 1)
print_size(f2, 2)
print_size(f3, 3)


# In[182]:

# Returns a dictionary of word-frequency pairs from the union of several feature sets
def union_choosen_features(*args):
    if (not all([type(arg) is set for arg in args])):
        raise ValueError('Input must be sets of word-frequency pairs.')
    if (len(args) < 2):
        raise ValueError('At least 2 arguments needed.')
    
    N = len(args)  # number of documents
    result = dict()  # word:frequency pairs
    for i in range(N):
        for w in args[i]:  # access each feature set
            if w[0] in result.keys():
                result[w[0]] += w[1]
            else:
                result[w[0]] = w[1]
    return result
        
union_features = union_choosen_features(f1, f2, f3)
print_size(union_features, '\"union features\"')
sorted(all_features.items(), key=lambda x: x[1], reverse=True)


# In[183]:

# The way to assign a sequence of variables (you can safely ignore this part)
for i in range(3):
    vars()[''.join(['arg', str(i)])] = ' '.join(['Integer', str(i)])
print(arg0, arg1, arg2)

