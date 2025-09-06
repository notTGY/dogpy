#!/usr/bin/env python3
from download_python_docs import download_python_docs
from dotenv import load_dotenv
import os
import argparse
from agents import agent


def main():
    parser = argparse.ArgumentParser(
        description="ask questions about Python documentation"
    )
    parser.add_argument(
        "--prompt", type=str, default="", help="prompt for non-interactive use"
    )
    args = parser.parse_args()

    download_python_docs()

    prompt = args.prompt or input("> ")
    result = agent.run(prompt)
    print(result)


if __name__ == "__main__":
    main()
