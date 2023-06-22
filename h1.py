import requests
import operator


url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
heroes_list = ['Hulk', 'Captain America', 'Thanos']
dictionaries = resp.json()

intelligence = []


for meaning in dictionaries:
    result = meaning['powerstats']['intelligence']
    if meaning['name'] in heroes_list:
        intelligence.append(result)

heroes_list_intelligence = dict(zip(heroes_list, intelligence))

maximum = max(heroes_list_intelligence, key = heroes_list_intelligence.get)
print(maximum)