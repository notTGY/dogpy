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


def get_top_level_dirs(paths):
    dirs = []
    for path in paths:
        top_level_dir = path.split("/", 2)[1]
        if top_level_dir and not top_level_dir in dirs:
            dirs.append(top_level_dir)
    dirs.sort()
    return dirs


def list_docs(version=DEFAULT_VERSION):
    output_path = f"{cache_path}/docs-{version}.zip"
    with zipfile.ZipFile(output_path, "r") as zip_ref:
        all_files = zip_ref.namelist()
        for dir in get_top_level_dirs(all_files):
            print(f"- {dir}")
    pass


if __name__ == "__main__":
    download_python_docs()
    list_docs()
