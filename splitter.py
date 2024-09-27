import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter

class split(RecursiveCharacterTextSplitter):
    def __init__(self, doc_list, overlap, chunk_size):
        super().__init__(overlap = overlap, chunk_size = chunk_size)
        self.doc_list = doc_list
    
    def get_doc_len(self):
        l_list = [len(doc) for doc in self.doc_list]
        return l_list

    def split_text(self):
        l_list = self.get_doc_len()
        doc_list = self.doc_list
        