import requests
from bs4 import BeautifulSoup


def get_list_items(hero):
    URL = f'https://www.dotabuff.com/heroes/{hero.lower()}'
    response = requests.get(URL, headers={'User-Agent' : 'test'}).text
    soup = BeautifulSoup(response, 'html.parser')
    item_stats =soup.find_all('tr', attrs={'data-link-to' : True})
    #print(item_stats)
    list_items = []
    

    for i in range(10):
        sp = item_stats[i].text
        string_new = sp[:-7] + '  ' + sp[-6:]
        #print(string_new)
        list_items.append(string_new)

    return list_items
