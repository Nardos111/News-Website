from newsapi import NewsApiClient
import json


def get_news(keyword):
    apiKey = "423b4fa3ae35431b927b27cdcf3bcace"  # Insert your api key here
    newsapi = NewsApiClient(apiKey)
    news = newsapi.get_everything(q=keyword, language='en', page_size=15)
    news_articles = news['articles']
    with open("./news.js", "w") as outfile:
        json.dump(news_articles, outfile, ensure_ascii=False)
    return "done"
