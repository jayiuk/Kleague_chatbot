import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter

class split(RecursiveCharacterTextSplitter):
    def __init__(self, doc_list, overlap, chunk_size = None, **kwargs):
        super().__init__(overlap = overlap, chunk_size = chunk_size, **kwargs)
        self.doc_list = doc_list

    def split_text(self):
        chunked_list = []
        for doc in self.doc_list:
            splitted_doc = doc.split("\n\n")
            self._chunk_size = len(splitted_doc)
            