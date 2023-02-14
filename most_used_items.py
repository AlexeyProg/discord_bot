import requests
from bs4 import BeautifulSoup


def get_list_items(hero):
    URL = f'https://www.dotabuff.com/heroes/{hero.lower()}'
    response = requests.get(URL, headers={'User-Agent' : 'test'}).text
    soup = BeautifulSoup(response, 'html.parser')
    item_stats =soup.find_all('tr', attrs={'data-link-to' : True})

    list_items = []

    for i in range(10):
        print(item_stats[i].text)
        list_items.append(item_stats[i].text)

    return list_items

