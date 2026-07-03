from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.retrievers import TFIDFRetriever
import tempfile
import os

def load_and_index_pdf(uploaded_file):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Load PDF
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    # Create TF-IDF retriever — no embeddings needed!
    retriever = TFIDFRetriever.from_documents(chunks)
    retriever.k = 3

    # Clean up temp file
    os.unlink(tmp_path)

    return retriever

def get_answer(retriever, question):
    llm = Ollama(model="llama3")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    result = qa_chain({"query": question})

    return {
        "answer": result["result"],
        "sources": result["source_documents"]
    }