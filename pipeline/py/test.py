import requests
import json
def dad_joke():
    joke = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'})
    joke = joke.json()['joke']
    return joke

print("Let me cheer you up with a joke: \n --------------------------------------")
print(dad_joke())
d = {}
for i in range(0,3):
    d[i] = dad_joke()
    
with open("jokes.json","w", encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
