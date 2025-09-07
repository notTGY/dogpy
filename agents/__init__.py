import os
from dotenv import load_dotenv
from smolagents import LogLevel, OpenAIServerModel, ToolCallingAgent

load_dotenv()

debug = True if os.getenv("DEBUG") else False
api_key = os.getenv("OPENROUTER_API_KEY")

model_id = "meta-llama/llama-3.1-8b-instruct" if api_key else "llama3.1:8b"
api_base = "https://openrouter.ai/api/v1" if api_key else "http://localhost:11434/v1"

instructions = """Answer question. Always include example with test data in answer.
Always query documentation for relevant information, base your answer on the retrieved documents."""

def create_agent(tools):
    model = OpenAIServerModel(
        model_id=model_id,
        api_base=api_base,
        api_key=api_key,
    )
    agent = ToolCallingAgent(
        tools=tools,
        model=model,
        stream_outputs=debug,
        verbosity_level=LogLevel.INFO if debug else LogLevel.ERROR,
        instructions=instructions,
    )
    return agent
