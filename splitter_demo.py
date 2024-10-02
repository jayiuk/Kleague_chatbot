import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter

class split(RecursiveCharacterTextSplitter):
    def __init__(self, doc_list, chunk_overlap:int = 0, chunk_size:int = 0, **kwargs):
        super().__init__(chunk_overlap = chunk_overlap, chunk_size = chunk_size, **kwargs)
        self.doc_list = doc_list

    def split_text(self):
        chunked_list = []
        chunked_doc_list = []
        doc_list = [doc.page_content for doc in self.doc_list]
        for doc in doc_list:
            splitted_doc = doc.split('\n\n')
            self.chunk_size = len(splitted_doc)
            self.chunk_overlap = self.chunk_size // 3
            for splitted_doc in doc:
                chunked_doc = splitted_doc.split('.')
                chunked_doc_list.append(chunked_doc)
            for _ in range()
        return chunked_list
                    
