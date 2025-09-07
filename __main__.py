#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import argparse

from agents import create_agent
from rag import prepare_python_docs, RetrieverTool


def main():
    parser = argparse.ArgumentParser(
        description="ask questions about Python documentation"
    )
    parser.add_argument(
        "--prompt", type=str, default="", help="prompt for non-interactive use"
    )
    args = parser.parse_args()

    retriever_tool = RetrieverTool(prepare_python_docs())
    agent = create_agent(tools=[retriever_tool])

    prompt = args.prompt or input("> ")
    result = agent.run(prompt)
    print(result)


if __name__ == "__main__":
    main()
