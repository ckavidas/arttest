import requests as r
from os import environ

def get_artifacts_list(info):
  uri = "{baseurl}/{user}/{repo}/actions/artifacts".format(
    baseurl=info['baseurl'],
    user=info['user'],
    repo=info['repo'],
  )
  req = r.get(uri, headers=info['headers'])
  results = {
    "Status_Code": req.status_code,
    "JSON": req.json(),
  }
  return results

def download_artifact(info, artifact_id):
  pass

def main():
  env = dict(environ)
  if 'INPUT_ACCESS-TOKEN' in env.keys():
    print("Access Token Key Exists")
    print(env['INPUT_ACCESS-TOKEN'][-1])
  info = {
    "repo": "arttest",
    "user": "ckavidas",
    "headers": {"Accept":"application/vnd.github.v3+json"},
    "baseurl": "https://api.github.com/repos",
  }
  artifacts = get_artifacts_list(info)['JSON']['artifacts']
  for artifact in artifacts:
    if artifact['name'] == 'jokes':
      print({artifact['id']:artifact['archive_download_url']})

if __name__ == "__main__":
  main()
