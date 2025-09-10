from smolagents import LogLevel, OpenAIServerModel, ToolCallingAgent, Tool

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

    def __init__(self, retriever, **kwargs):
        super().__init__(**kwargs)

        self.retriever = retriever

    def forward(self, query: str) -> str:
        """Execute the retrieval based on the provided query."""
        assert isinstance(query, str), "Your search query must be a string"

        return self.retriever.query(query)

instructions = """Answer question. Always include example with test data in answer.
Always query documentation for relevant information, base your answer on the retrieved documents."""

def create_agent(model, api_key, api_base, retriever, debug=False):
    _model = OpenAIServerModel(
        model_id=model,
        api_base=api_base,
        api_key=api_key,
    )
    tools = [
        RetrieverTool(retriever)
    ]
    agent = ToolCallingAgent(
        tools=tools,
        model=_model,
        stream_outputs=debug,
        verbosity_level=LogLevel.INFO if debug else LogLevel.ERROR,
        instructions=instructions,
    )
    return agent
