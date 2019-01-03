import json as js
import requests

#initial
riot_key = '?api_key=RGAPI-aa0aefda-f5e8-4407-a5c0-35c146960e59'
summoner = 'JetNOVA'
server = 'https://na1.api.riotgames.com'
command = '/lol/summoner/v3/summoners/by-name/'

def get_champ_mastery():
    command = "/lol/champion-mastery/v3/champion-masteries/by-summoner/"
    url = server + command + summoner + riot_key
    r = requests.get(url)
    print(r.encoding).json()
    print(r.encoding)

def run_command():
    url = server + command + summoner + riot_key
    r = requests.get(url).json()
    print(r)
#Various commands can be pulled of the riot site depending on what information you are looking for. There are many static commands which should be downloaded locally rather than repeatedly utilizing for all API pulls
#LOL STATIC DATA includes everything that only changes on a patch by patch rather than match by match basis.
summoner = 'JetNOVA'
#run_command()
get_champ_mastery()
run_command()
summoner = 'White Ezreal'
run_command()

