from bs4 import BeautifulSoup
import requests
from time import sleep

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
                div_puns = [pun.getText() for pun in div.findAll('p')]
                page_puns.extend(div_puns)
            puns.extend(page_puns)
    return puns
