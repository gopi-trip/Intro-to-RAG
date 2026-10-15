# File responsible for storing the pdf file.
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent / "data" / "sample.pdf"
print(f"Loading PDF file from: {pdf_path}")
# PDF Loading
loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

#Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
chunks = text_splitter.split_documents(docs) 

#Make the embeddings
embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

#Make the vector db store
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="sample_collection",
    url="http://localhost:6333",
    force_recreate=True  # Set to True to recreate the collection if it already exists
)

print("PDF file has been processed and vector store generated.")
