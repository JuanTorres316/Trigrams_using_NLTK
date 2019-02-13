import nltk
from nltk.corpus import stopwords
import pandas
import itertools
from nltk import sent_tokenize, word_tokenize



english_Stopwords = stopwords.words('english')
data = pandas.read_csv('/Users/Juan/Desktop/complaint_tool/CSV_File_Manipulation/Consumer_Complaints.csv')

narrative = data['Consumer complaint narrative']
sentences = []
words = []


for x in narrative:
    sentence = sent_tokenize(x)
    sentences.append(sentence)
    word = word_tokenize(x)
    words.append(word)


flattened_words = list(itertools.chain.from_iterable(words))
cleaned_Words = [x for x in flattened_words if x not in english_Stopwords] 
cleaned_Words = [x for x in cleaned_Words if len(x) > 2]
tagged_words = nltk.pos_tag(cleaned_Words) 

#below is code for identifying named entities with NLTK - going to make it better
named_Ent = nltk.ne_chunk(tagged_words)
print(named_Ent)

#tagged_words = dict(tagged_words)



