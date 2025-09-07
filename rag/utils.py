import platform
import requests
import os
import zipfile

DEFAULT_VERSION = platform.python_version()
cache_path = ".cache"

def download_python_docs(version=DEFAULT_VERSION):
    output_path = f"{cache_path}/docs-{version}.zip"
    os.makedirs(cache_path, exist_ok=True)
    try:
        open(output_path, "r")
    except FileNotFoundError:
        print(f"Downloading docs for python{version}")
        response = requests.get(
            f"https://docs.python.org/ftp/python/doc/{version}/python-{version}-docs-text.zip"
        )
        response.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive new chunks
                    f.write(chunk)
    return output_path


def get_top_level_dirs(paths):
    dirs = []
    for path in paths:
        top_level_dir = path.split("/", 2)[1]
        if top_level_dir and not top_level_dir in dirs:
            dirs.append(top_level_dir)
    dirs.sort()
    return dirs


def list_docs(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        all_files = zip_ref.namelist()
        for dir in get_top_level_dirs(all_files):
            print(f"- {dir}")
    pass

def get_files_from_dir(dirname, file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        all_files = zip_ref.namelist()
        files = {}
        for path in all_files:
            top_level_dir = path.split("/", 2)[1]
            if top_level_dir == dirname:
                with zip_ref.open(path) as file:
                    files[path] = str(file.read())
        return files

def prepare_python_docs():
    docs_path = download_python_docs()
    files = get_files_from_dir("library", docs_path)
    texts = []
    for fname in files:
        texts.append(files[fname])
    return texts
