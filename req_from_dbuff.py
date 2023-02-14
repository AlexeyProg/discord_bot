import requests
from bs4 import BeautifulSoup

URL = 'https://www.dotabuff.com/heroes/winning'
list_heroes = []
list_winrates = []

def get_tuple_winrates():
    req = requests.get(URL, headers={'User-agent' : 'test'}).text
    s = BeautifulSoup(req, 'html.parser')

    test = s.find_all('td', attrs={'data-value' : True})
    # for index in test:
    #     print(index['data-value'])

    for item in range(0,40,4):
        list_heroes.append(test[item]['data-value'])
        list_winrates.append(test[item+1]['data-value'])

    result = dict(zip(list_heroes,list_winrates))  #два списка объединяем в словарь

    return result

# test = get_tuple_winrates()

# for k,v in test.items():
#     print(f'- - - {k} - {v}')