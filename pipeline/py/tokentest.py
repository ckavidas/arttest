import os

token = os.getenv('GITHUB_TOKEN')

if token:
    print(len(token))
