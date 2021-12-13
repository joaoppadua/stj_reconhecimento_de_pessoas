#New version of script to get news from Bolsonaro and Covid

from GoogleNews import GoogleNews
import pandas as pd, datetime


date_object = datetime.date.today()
google_news = GoogleNews()
google_news.set_lang('pt')
google_news.set_time_range('04/01/2020', (date_st := date_object.strftime('%d/%m/%Y'))
google_news.set_encode('utf-8')

def get_news(search_param, rng=20):
    google_news.search(search_param)
    result=google_news.result()
    df = pd.DataFrame(result)
    for i in range(2, rng):
        google_news.get_page(i)
        result = google_news.result()
        df.append(result)
    return df

data = get_news('Bolsonaro covid')
print(data.head())

data.to_csv('/home/jppadua/bolsonaro.csv')
