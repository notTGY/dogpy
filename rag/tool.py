from langchain_community.retrievers import BM25Retriever
from smolagents import Tool

class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses semantic search to retrieve the parts of python documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
        }
    }
    output_type = "string"

    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_texts(
            docs, k=1
        )

    def forward(self, query: str) -> str:
        """Execute the retrieval based on the provided query."""
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.retriever.invoke(query)

        return docs[0]
