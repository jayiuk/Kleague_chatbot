import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter

class split(RecursiveCharacterTextSplitter):
    def __init__(self, doc_list, chunk_overlap:int = 0, chunk_size:int = 0, **kwargs):
        super().__init__(chunk_overlap = chunk_overlap, chunk_size = chunk_size, **kwargs)
        self.doc_list = doc_list

    def split_text(self):
        chunked_list = []
        i = 0
        doc_list = [doc.page_content for doc in self.doc_list]
        for doc in doc_list:
            splitted_doc = doc.split('\n\n')
            self.chunk_size = len(splitted_doc)
            self.chunk_overlap = self.chunk_size // 3
            for i in range(len(splitted_doc)):
                if i == 0:
                    splitted = splitted_doc[i]
                    chunked = splitted
                else:
                    splitted = splitted_doc[i]
                    splitted_before = splitted_doc[i-1]
                    overlaped = splitted_before[-self.chunk_overlap:]
                    chunked = overlaped + splitted
                chunked_list.append(chunked)

        return chunked_list
                    
