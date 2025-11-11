from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import TextSplitter,RecursiveCharacterTextSplitter,CharacterTextSplitter,TokenTextSplitter
loader=TextLoader('/home/sourav/rag-course-krishnaik/documents/sample.txt',encoding='utf-8')
documents=loader.load()
print(documents)
#character text splitter
splitter=CharacterTextSplitter(
    separator="\n",
    chunk_size=10,
    chunk_overlap=2,
    length_function=len
)
content_chunks=splitter.split_text(documents[0].page_content)
print(content_chunks)

#recursive character text splitter
recursive_splitter=RecursiveCharacterTextSplitter(
    separators=["\n"," ",""],
    chunk_size=10,
    chunk_overlap=2,
    length_function=len
)
content_chunks_recursive=recursive_splitter.split_text(documents[0].page_content)
print(content_chunks_recursive)

#token text splitter
token_splitter=TokenTextSplitter(
    chunk_size=10, 
    chunk_overlap=2
    )

content_chunks_tokens=token_splitter.split_text(documents[0].page_content)
print(content_chunks_tokens)