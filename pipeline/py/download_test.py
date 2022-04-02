import requests as r

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

def main():
  info = {
    "repo": "arttest",
    "user": "ckavidas",
    "headers": {"Accept":"application/vnd.github.v3+json"},
    "baseurl": "https://api.github.com/repos",
  }
  test = get_artifacts_list(info)
  print(test)
