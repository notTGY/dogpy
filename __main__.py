#!/usr/bin/env python3
import platform
from download_python_docs import download


def main():
    version = platform.python_version()
    download()


if __name__ == "__main__":
    main()
