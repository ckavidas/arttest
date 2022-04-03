import os
import sys

print(len(sys.argv))
print(sys.argv[0][-1])
token = os.environ.get('GITHUB_TOKEN')
print(type(token))
