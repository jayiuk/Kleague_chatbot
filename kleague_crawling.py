from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

class crawler():

    def __init__(self, url):
        self.url = url
    
    def get_url(self):
        url = self.url
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        att = soup.find_all('a', attrs = {"localName" : "li"})
        print(att)
        return att