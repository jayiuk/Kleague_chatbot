import langchain
import langchain_core
import langsmith
from langchain_community.document_loaders import SeleniumURLLoader


class document_loader():
    def __init__(self, df):
        self.df = df
    
    def url_load(self):
        df = self.df
        urls = []
        for url in df['link']:
            urls.append(url)
        return urls
    
    def url2doc(self):
        urls = self.url_load()
        sul = SeleniumURLLoader(urls = urls, browser = 'chrome', continue_on_failure = True, headless = True)
        url_docs = sul.load_and_split()
        return url_docs