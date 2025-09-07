from .utils import prepare_python_docs
from .tool import RetrieverTool

if __name__ == "__main__":
    docs = prepare_python_docs()
    tool = RetrieverTool(docs)
    res = tool("how to append to a list")
    print(res)
