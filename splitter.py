import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter

class split(RecursiveCharacterTextSplitter):
    def __init__(self, doc_list, chunk_overlap = None, chunk_size = None, **kwargs):
        super().__init__(chink_overlap = chunk_overlap, chunk_size = chunk_size, **kwargs)
        self.doc_list = doc_list

    def split_text(self):
        chunked_list = []
        i = 0
        for doc in self.doc_list:
            splitted_doc = doc.split("\n\n")
            self.chunk_size = len(splitted_doc)
            self.chunk_overlap = self.chunk_size // 4
            overlaped = splitted_doc[-self.chunk_overlap]
            for i in range(self.chunk_size):
                doc_zip = zip(splitted_doc[i], overlaped[i-1])
                if i == 0:
                    doc_zip = splitted_doc
                chunked_list.append(doc_zip)
        return chunked_list
            