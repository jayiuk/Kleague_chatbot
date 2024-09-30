import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter

class split(RecursiveCharacterTextSplitter):
    def __init__(self, doc_list, chunk_overlap:int = 0, chunk_size:int = 0, **kwargs):
        super().__init__(chunk_overlap = chunk_overlap, chunk_size = chunk_size, **kwargs)
        self.doc_list = doc_list

    def split_text(self):
        chunked_list = []
        splitted_list = []
        overlap_list = []
        i = 0
        doc_list = [doc.page_content for doc in self.doc_list]
        for doc in doc_list:
            splitted_doc = doc.split("\n\n")
            splitted_list.append(splitted_doc)
            self.chunk_size = len(splitted_doc)
            self.chunk_overlap = self.chunk_size // 4
            overlaped = splitted_list[-self.chunk_overlap]
            overlap_list.append(overlaped)
        for i in range(len(doc_list)):
            doc_zip = zip(splitted_list[i], overlap_list[i-1])
            doc_zip = list(doc_zip)
            if i == 0:
                doc_zip = splitted_list[i]
            chunked_list.append(doc_zip)
        return chunked_list
            