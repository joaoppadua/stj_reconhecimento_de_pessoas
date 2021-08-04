#Script to create a corpus of Bolsonaro and covid

from GoogleNews import GoogleNews
from datetime import datetime
import linguistics
import nltk

news = GoogleNews(lang='pt', period='1y')

def get_data(param):
    news.get_news(param)
    compData = news.results(sort=True)
    headers = news.get_texts()
    sources = news.get_links()
    return compData, headers, sources

data, headers, sources = get_data('bolsonaro')
corpus = ' '.join(headers)
tokenized_corpus = nltk.word_tokenize(corpus)
T = nltk.Text(tokenized_corpus)
clean_corpus = linguistics.clean_txt(corpus, 'portuguese', stop=False)
typeToken, collocations, frequecy_distribution = linguistics.text_basics(clean_corpus)

print(collocations)

T.concordance('cloroquina')

print(len(tokenized_corpus))
print(len(clean_corpus))
#print(headers[0])
#print(data[0])