import os

scpath = os.environ.get('script-path')
token = os.environ.get('access-token')

print(type(scpath))
print(type(token))
if scpath:
  print(scpath)

if token:
  print(token[-1])
