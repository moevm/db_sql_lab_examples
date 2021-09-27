import json

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from pydash import uniq, sort, get


def get_codes():
    results = {}

    for i in tqdm(range(301, 999)):
        url = f'https://region-operator.ru/{i}'

        operators = []
        regions = []

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')

        if not table:
            print(f'{i} not exists')
            continue

        x = (len(table.findAll('tr')) - 1)

        for row in table.findAll('tr')[1:x]:
            col = row.findAll('td')
            operators.append(col[1].text)
            regions.append(col[2].text)

        results[i] = {
            'regions': sort(uniq(regions)),
            'operators': sort(uniq(operators))
        }

    with open('codes.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False)



phones = {}
for i in tqdm(range(9000000000, 9999999999)):
    url = f'https://region-operator.ru/{i}'


    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    location = ''
    location_p = soup.find('p', {'style': 'text-align: center; color: red;'})
    if location_p:
        location = location_p.text.replace('>', '').replace('<', '').strip()

    operator = ''
    operator_p = soup.find('p', {'class': 'actualOp'})
    if operator_p:
        operator = operator_p.text.replace('>', '').replace('<', '').strip()

    url = f'https://region-operator.ru/{i}-check'

    r = requests.get(url)

    p = get(r.json(), '0.moved2operator')
    if p:
        operator = p

    if operator and location:
        phones[i] = {
            'operator': operator,
            'location': location
        }

    if i % 10000 == 0:
        with open(f'phones_{i}.json', 'w') as f:
            json.dump(phones, f, ensure_ascii=False)

with open(f'phones_{i}.json', 'w') as f:
    json.dump(phones, f, ensure_ascii=False)