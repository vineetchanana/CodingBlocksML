from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

tokenizer = RegexpTokenizer(r'\w+')
stemmer = PorterStemmer()
sw = set(stopwords.words('english'))

def stemmed_review(review):
    review = review.lower()  #convert to lower
    review = review.replace('<br /><br />',' ') #remove br tags that won't be removed by stopwords
    tokens = tokenizer.tokenize(review) #convert it into smallest unit
    filtered_tokens = [w for w in tokens if w not in sw or w =='not'] # remove stopwords
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens] #stemming
    
    cleaned_review = ' '.join(stemmed_tokens)
    
    return cleaned_review


