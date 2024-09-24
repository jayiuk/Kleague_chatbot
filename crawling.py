import pandas as pd
import requests
from bs4 import BeautifulSoup

class get_news():
    def __init__(self, url):
        self.url = url
    
    def get_kleague_news(self):
        base_url = self.url
        page = 1
        news_list = []
        while True:
            print(f"크롤링 중인 페이지 : {page}")
            url = base_url + '&page=' + str(page)
            response = requests.get(url)
            if response.status_code != 200:
                print("크롤링 종료")
                break
            soup = BeautifulSoup(response.text, 'html.parser')
            news_elements = soup.select('ul.thum-list.f-wrap a')
            if not news_elements:
                print("크롤링 끝")
                break
            for news in news_elements:
                link = news.get('href')
                if link:
                    real_url = f"https://www.kleague.com{link}"
                    if real_url in news_list:
                        print("크롤링 끝")
                        break
                    news_list.append(real_url)
                    
            page += 1
        return news_list

    def get_df(self):
        news_list = self.get_kleague_news()
        df = pd.DataFrame({'link' : news_list})
        return df