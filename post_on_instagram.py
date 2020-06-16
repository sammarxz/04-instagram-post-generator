import os
from instapy_cli import client


username = os.environ.get('INSTAGRAM_USERNAME')
password = os.environ.get('INSTAGRAM_PASSWORD')


def post(filename, text):
    with client(username, password) as cli:
        cli.upload('./posts/{}'.format(filename), text)
