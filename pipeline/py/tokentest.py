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

def download_artifact(info, download_link):
  headers=info['headers']
  zip_file = r.get(download_link, headers=headers)
  with open("downloaded_from_python.zip", "wb") as f:
    f.write(zip_file.content)
    f.close()

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
  jokezips = []
  for artifact in artifacts:
    if artifact['name'] == 'jokes':
      jokezips.append(artifact['archive_download_url'])
  print("lets try to download the first zip")
  download_artifact(info, jokezips[0])


if __name__ == "__main__":
  main()
