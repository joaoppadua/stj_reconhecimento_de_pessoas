#Script to parse Bolsonaro media

from newspaper import Article
import nltk, pandas as pd, os

def parse_media(data):
    data_l = list()
    for i in data.index:
        dic = dict()
        a = Article(data['link'][i], language='pt')
        a.download()
        a.parse()
        a.nlp()
        dic['Date'] = data['date'][i]
        dic['Media'] = data['media'][i]
        dic['Title'] = a.title
        dic['Text'] = a.text
        dic['Summary'] = a.summary
        data_l.append(dic)
    return data_l

bolso_data_path = input('Enter file path: ')
bolso_data = pd.read_csv(os.path.join(bolso_data_path, 'bolsonaro.csv'))
bolso_df = pd.DataFrame(parse_media(bolso_data))
print(bolso_df['Date'])