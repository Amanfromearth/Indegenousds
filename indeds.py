from newsapi import NewsApiClient
from transformers import pipeline

newsapi = NewsApiClient(api_key= '6972a8a222224795a3ac0148ec506a1b')

top_headlines = newsapi.get_top_headlines(language='en',country='in')

sentiment_pipeline = pipeline("sentiment-analysis")

res ={}

for i in range(len(top_headlines["articles"])):
    text = top_headlines["articles"][i]["description"]
    senti = sentiment_pipeline(text)[0]['label']
    article = top_headlines["articles"][i]["title"]
    res[article] = senti
    
print(res)

