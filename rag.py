# import packages
import os 
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
import ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Function to read PDF documents
def load_pdf_text(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Specify the directory containing the PDF files
pdf_directory = "./input_data"

# Get a list of all PDF files in the directory
pdf_paths = [os.path.join(pdf_directory, file) for file in os.listdir(pdf_directory) if file.endswith('.pdf')]


# Extract the text
docs = [load_pdf_text(pdf) for pdf in pdf_paths]

# Combine all text into a single document
combined_text = "\n".join(docs)


# Split the combined text into chunks for better retrieval
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_text(combined_text)


# Create Ollama embeddings
embeddings = OllamaEmbeddings(model="llama3.1")

# Create a vector store from the documents and embeddings
vectorstore = Chroma.from_texts(texts=splits, embedding=embeddings)

# Function to interact with the LLaMA 3 model using Ollama
def ollama_llm(question, context):
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    response = ollama.chat(model='llama3.1', messages=[
        {'role': 'system', 'content': 'You are a helpful SQL ai assistant that helps students answer sql qeustions. You respond appropriately and give examples where necessary.'},
        {'role': 'user', 'content': 'What is SQL?'},
        {'role': 'assistant', 'content': 'SQL stands for Structured Query Language!'},
        {'role': 'user', 'content': formatted_prompt}
        ])
    return response['message']['content']

# Convert retrieved documents into a single formatted context string
def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# RAG chain to get answers
def rag_chain(question):
    # Retrieve relevant documents
    retriever = vectorstore.as_retriever()
    retrieved_docs = retriever.invoke(question)
    
    # Combine retrieved documents into context
    formatted_context = combine_docs(retrieved_docs)
    
    # Generate answer using LLaMA 3 model
    return ollama_llm(question, formatted_context)

# Test the RAG setup
# result = rag_chain("Tell me something random")
# print(result)