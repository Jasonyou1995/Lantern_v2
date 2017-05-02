
# coding: utf-8

# In[84]:

# import nltk
# nltk.download()


# In[111]:

# Import packages and read from ./data repo
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
corpus_root = 'data/SH_data'
wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')
ids = wordlists.fileids()

# use three documents as samples
corp = {}
for x in range(0,10):
    corp["d{0}".format(x)]=wordlists.words(ids[x])


# In[114]:

corp["d0"]


# In[116]:

print(stopwords.readme())

# Get the frequency distribution for each document
fd = {}
for x in range(0,10):
    fd["fd{0}".format(x)]=nltk.FreqDist(corp["d{0}".format(x)])

# the words that only shown once
print(
    len(fd['fd1'].hapaxes()),
    len(fd['fd2'].hapaxes()),
    len(fd['fd3'].hapaxes()),
    )


# In[117]:

# most common words before cleaning
print(fd['fd1'].most_common(10))
print(fd['fd2'].most_common(10))
print(fd['fd3'].most_common(10))


# In[118]:

my_stopwords = set(['the', 'a', '.', 'studies', 'students', 'schools', 'prevalence', 'national', 'general', 'whether', 'statistically', 'probabilities', 'covered', 'subject', 'associated', 'indicate', 'testing'])  # we can define our own stop words in here


# In[122]:

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
f = {}
for x in range(0,10):
    f["f{0}".format(x)]=feature_extractor("d{0}".format(x), fd['fd{0}'.format(x)], 7, 7, my_stopwords)

print_size(f['f1'], 1)
print_size(f['f2'], 2)
print_size(f['f3'], 3)


# In[121]:

# Returns a dictionary of word-frequency pairs from the union of several feature sets
def union_choosen_features(setlist):
#     if (not all([type(arg) is set for arg in args])):
#          raise ValueError('Input must be sets of word-frequency pairs.')
#     if (len(args) < 2):
#         raise ValueError('At least 2 arguments needed.')
    N = len(setlist)  # number of documents
    result = dict()  # word:frequency pairs
    for i in range(N):
        for w in setlist[i]:  # access each feature set
            if w[0] in result.keys():
                result[w[0]] += w[1]
            else:
                result[w[0]] = w[1]
    return result
       
union_features = union_choosen_features(f.values())
print_size(union_features, '\"union features\"')
sorted(union_features.items(), key=lambda x: x[1], reverse=True)


# In[183]:

# The way to assign a sequence of variables (you can safely ignore this part)
for i in range(3):
    vars()[''.join(['arg', str(i)])] = ' '.join(['Integer', str(i)])
print(arg0, arg1, arg2)


# In[ ]:

def main():
    #create the dictionary
    keys = ["Drug", "Harrass", "Bullying", "Assault", "Vandalism"]
    paths = ["data/drug_data", "data/SH_data", "data/bully_data", "data/assault_data", "data/vandalism_data"]
    all_data = {}
    for path in paths:
        z = 0
        corpus_root = path
        wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')
        ids = wordlists.fileids()

        # collect all the documents from the folder
        corp = {}
        for x in range(0,10):
            corp["d{0}".format(x)]=wordlists.words(ids[x])

        fd = {}
        for x in range(0,10):
            fd["fd{0}".format(x)]=nltk.FreqDist(corp["d{0}".format(x)])
        
        f = {}
        for x in range(0,10):
            f["f{0}".format(x)]=feature_extractor("d{0}".format(x), fd['fd{0}'.format(x)], 7, 7, my_stopwords)
        
        union_features = union_choosen_features(f.values())
        print_size(union_features, '\"union features\"')
        all_data[keys[z]] = sorted(union_features.items(), key=lambda x: x[1], reverse=True)
        z+=1
main()  
print(all_data)


