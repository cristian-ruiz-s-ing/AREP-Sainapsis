import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone

def cargar():
    pinecone.init(api_key= "8209dc1d-c0e1-40ba-b45d-c6bf46ad5fa5",
    environment= "gcp-starter")

    embeddings = OpenAIEmbeddings()
    text = open("./documentos/economia.txt", "r", encoding="utf-8")
    data = Pinecone.from_texts(texts=[text.read()],
    embedding=embeddings,
    index_name="tallersainapsis")

    text = open("./documentos/ingenieria-civil.txt", "r", encoding="utf-8")
    data = Pinecone.from_texts(texts=[text.read()],
    embedding=embeddings,
    index_name="tallersainapsis")

    text = open("./documentos/ingenieria-electrica.txt", "r", encoding="utf-8")
    data = Pinecone.from_texts(texts=[text.read()],
    embedding=embeddings,
    index_name="tallersainapsis")

    text = open("./documentos/ingenieria-electronica.txt", "r", encoding="utf-8")
    data = Pinecone.from_texts(texts=[text.read()],
    embedding=embeddings,
    index_name="tallersainapsis")

    text = open("./documentos/ingenieria-industrial.txt", "r", encoding="utf-8")
    data = Pinecone.from_texts(texts=[text.read()],
    embedding=embeddings,
    index_name="tallersainapsis")

    text = open("./documentos/ingenieria-sistemas.txt", "r", encoding="utf-8")
    data = Pinecone.from_texts(texts=[text.read()],
    embedding=embeddings,
    index_name="tallersainapsis")


def buscar():
    pinecone.init(api_key= "8209dc1d-c0e1-40ba-b45d-c6bf46ad5fa5",
    environment= "gcp-starter")
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index("tallersainapsis",
    embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de sistemas?"
    docs = docsearch.similarity_search(query)
    print(docs)


buscar()