import pandas as pd
import numpy as np
import seaborn
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import os
import urllib.request
class get_news():
    def __init__(self, url):
        self.url = url
    
    def get_kleague_news(self):
        client_id = os.getenv('naver_api_id')
        client_secret = os.getenv('naver_api_pw')
        encText = urllib.parse.quote('k리그')
        url = self.url + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header('X-Naver-Client-Secret', client_secret)
        