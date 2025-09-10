#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import time
import argparse
from agents import create_agent
from rag import *
from dotenv import load_dotenv
load_dotenv()

debug = True if os.getenv("DEBUG") else False
api_key = os.getenv("OPENROUTER_API_KEY")

model = "meta-llama/llama-3.1-8b-instruct" if api_key else "llama3.2"
api_base = "https://openrouter.ai/api/v1" if api_key else "http://localhost:11434/v1"

api_key = api_key or "ollama"

embedding_model = "nomic-embed-text"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ask questions about Python documentation"
    )
    parser.add_argument(
        "--prompt", type=str, default="", help="prompt for non-interactive use"
    )
    parser.add_argument(
        "--model", type=str, default="", help="model"
    )
    args = parser.parse_args()
    if args.model:
        model = args.model

    start_time = time.time()

    retriever = Retriever(
        prepare_python_docs(),
        model=embedding_model,
    )
    agent = create_agent(model, api_key, api_base, retriever, debug)

    prompt = args.prompt or input("> ")
    result = agent.run(prompt)
    print(result)
    time_difference = time.time() - start_time
    print(f"took {time_difference:.2f}s")
