import langchain
import langchain_core
import langsmith
from langchain_community.document_loaders import SeleniumURLLoader


class document_loader():
    def __init__(self, list):
        self.list = list

    def url2doc(self):
        url_list = self.list
        sul = SeleniumURLLoader(url_list)