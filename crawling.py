import pandas as pd
import numpy as np
import os
import urllib.request
import json

class get_news():
    def __init__(self, url):
        self.url = url
    
    def get_kleague_news(self):
        client_id = os.getenv('naver_api_id')
        client_secret = os.getenv('naver_api_pw')
        encText = urllib.parse.quote('k리그')
        display = 100
        url = self.url + encText + '&display=' + str(display) + '&sort=date'
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header('X-Naver-Client-Secret', client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            res = response_body.decode('utf-8')
            response_fin = json.loads(res)
            return response_fin
        else:
            print("Error Code : ", rescode)
    
    def to_df(self, response):
        res = response['items']
        df = pd.DataFrame(columns = ['title', 'link', 'description', 'pubdate'])
        df_list = []
        for data in res:
            df_list.append(data)
        df_con = pd.DataFrame(df_list)
        return df_con