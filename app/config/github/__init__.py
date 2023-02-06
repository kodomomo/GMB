import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def _pem_file_content():
    pem_file_path = os.environ['PEM_FILE_PATH']

    with open(pem_file_path, 'rb') as file:
        return file.read()


# Github APP
PEM_CONTENT = _pem_file_content()
GITHUB_APP_ID = int(os.environ['GITHUB_APP_ID'])
ALGORITHM = 'RS256'