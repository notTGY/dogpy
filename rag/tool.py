from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

cache_path = ".cache"

class Retriever:
    def __init__(self, raw_docs, model="bm25"):
        source_docs = [Document(page_content=content) for content in raw_docs]
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=8192,
            chunk_overlap=50,
            add_start_index=True,
            strip_whitespace=True,
            separators=["\n\n", "\n", ".", " ", ""],
        )
        docs_processed = text_splitter.split_documents(source_docs)


        if model == "bm25":
            self.retriever = BM25Retriever.from_documents(
                docs_processed, k=2
            )
        else:
            embeddings = OllamaEmbeddings(model=model)
            output_path = f"{cache_path}/vs-{model}"
            try:
                open(output_path, "r")
                vectorstore = InMemoryVectorStore.load(output_path, embeddings)
            except FileNotFoundError:
                print(f"About to embed {len(docs_processed)} documents")
                vectorstore = InMemoryVectorStore.from_documents(
                    docs_processed,
                    embedding=embeddings,
                )
                vectorstore.dump(output_path)

            self.retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    def query(self, query: str) -> str:
        docs = self.retriever.invoke(query)

        return "\nRetrieved documents:\n" + "".join(
            [
                f"\n\n===== Document {str(i)} =====\n" + doc.page_content
                for i, doc in enumerate(docs)
            ]
        )
