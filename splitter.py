import langchain
from langchain_text_splitters import TextSplitter

class split(TextSplitter):
    def __init__(self, doc_list, overlap, length, chunk_size = None):
        super(split, self).__init__()
        self.doc_list = doc_list
        self.overlap = overlap
        self.length = len(self.doc_list)
        self.chunk_size = chunk_size
    
    def __len__(self):
        l_list = []
        for doc in self.doc_list:
            l = len(doc)
            l_list.append(l)
        return l_list

    def text_split(self):
        i = 0
        for i in self.length:
            