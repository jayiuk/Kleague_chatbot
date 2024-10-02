import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter

class split(RecursiveCharacterTextSplitter):
    def __init__(self, doc_list, chunk_overlap:int = 0, chunk_size:int = 0, **kwargs):
        super().__init__(chunk_overlap = chunk_overlap, chunk_size = chunk_size, **kwargs)
        self.doc_list = doc_list

    def split_text(self):
        chunked_list = []
        doc_list = [doc.page_content for doc in self.doc_list]
        for doc in doc_list:
            splitted_doc = doc.split('\n\n')
            self.chunk_size = len(splitted_doc)
            self.chunk_overlap = self.chunk_size // 3
            chunked_list.append(splitted_doc)
            for _ in splitted_doc:
                overlaped = splitted_doc[-self.chunk_overlap:]
                chunked = overlaped + splitted_doc
                if splitted_doc[0] == True:
                    chunked = splitted_doc
                chunked_list.append(chunked)

        return chunked_list
                    
