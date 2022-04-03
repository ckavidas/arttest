import os

env = dict(os.environ).keys()
token = dict(os.environ)['INPUT_ACCESS-TOKEN']
print(token[-1])


#scpath = os.environ.get('SCRIPT-PATh')
#token = os.environ.get('access-token')

#print(type(scpath))
#rint(type(token))
#if scpath:
#  print(scpath)

#if token:
# print(token[-1])
