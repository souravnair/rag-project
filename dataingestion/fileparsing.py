from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader, UnstructuredPDFLoader

#pypdf loader
pdf_loader=PyPDFLoader('/home/sourav/rag-course-krishnaik/documents/attention.pdf')
pdf_documents=pdf_loader.load()
print(pdf_documents)


#pymupdf is usually faster than pydf library and image extraction support is also provided in pymupdf, hence use pymupdf when you need faster processing, good text extraction and image extraction support.
print("".center(100,"-"))
pymupdf_loader=PyMuPDFLoader('/home/sourav/rag-course-krishnaik/documents/attention.pdf')
pymupdf_docs=pymupdf_loader.load()
print(pymupdf_docs)