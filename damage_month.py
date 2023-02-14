import requests
from bs4 import BeautifulSoup

URL = 'https://www.dotabuff.com/heroes/damage'

def get_hero_damage():
    req = requests.get(URL, headers = {'User-Agent' : 'test'}).text
    soup = BeautifulSoup(req, 'html.parser')

    hero_list = []
    damage_list = []
    hero_soup = soup.find_all('a', class_ = 'link-type-hero')
    for i in range(10):
        hero_list.append(hero_soup[i].text)
    
    request = soup.find_all('td', attrs={'data-value' : True})
    for i in range(1,40,4):
        damage_list.append(request[i].text)

    dict_hero_damage = dict(zip(hero_list,damage_list))
    return dict_hero_damage

