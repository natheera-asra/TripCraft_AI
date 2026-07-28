
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import os


DATA_PATH = "data/TRIPCRAFT-DATA"


def create_retriever():

    print("Loading PDFs...")


    loader = PyPDFDirectoryLoader(DATA_PATH)

    documents = loader.load()


    print("PDF documents:", len(documents))


    if len(documents) == 0:
        raise ValueError("No PDF files found. Check DATA_PATH")


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )


    chunks = splitter.split_documents(documents)


    print("Total chunks:", len(chunks))


    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )


    retriever = vector_db.as_retriever(
        search_kwargs={
            "k":4
        }
    )


    print("Retriever ready")


    return retriever
