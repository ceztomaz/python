import nltk
import numpy as np
import random
import string # to process standard python strings
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


#opening the document, read mode and ignoring erros
f=open('chatbot.txt','r',errors = 'ignore')

# read the content of a object as settled in the previous step
raw=f.read()

#converts into lowercase
raw=raw.lower()

nltk.download('punkt') #first time use only
nltk.download('wordnet') #first time use only

sent_tokens = nltk.sent_tokenize(raw) #convert to list of sentences
word_tokens = nltk.word_tokenize(raw) # convert to list of words

print(sent_tokens[:2])

lemmer=nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

greetings_input = ("hello","hi","greetings","sup","faaalaa","wazup","hey")

gretings_response=("hi","hey","*nods*","hi there","hello","i am glad you are talkgi to me","e ai rapá")

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greetings_input:
            return random.choice(gretings_response)


