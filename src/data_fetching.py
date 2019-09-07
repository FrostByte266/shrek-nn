from bs4 import BeautifulSoup
import re
import requests
from random import shuffle
from time import sleep
from sys import argv

def fetch_puns_list(num_pages):
    base_url = 'https://onelinefun.com/puns/{page}/'
    puns = []
    for page in range(1, num_pages+1):
        url = base_url.format(page=page)
        request = requests.get(url)
        if request.status_code != 200:
            raise RuntimeError(f'Attempt to request page #{page} returned an invalid response code: {request.status_code}')
        else:
            page_puns = []
            soup = BeautifulSoup(request.content, 'html.parser')
            for div in soup.findAll('div', {'class': 'o'}):
                regex = re.compile(r"""([\"'])(?:(?=(\\?))\2.)*?\1""")
                div_puns = [[pun.getText(), 1] if not re.match(regex, pun.getText()) else None for pun in div.findAll('p')]
                page_puns.extend(div_puns)
            puns.extend(page_puns)
    puns = [item for item in puns if item]
    return puns
