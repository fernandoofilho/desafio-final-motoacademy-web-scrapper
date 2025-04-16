import requests
from time import sleep
from config.settings import DELAY_BETWEEN_REQUESTS

def make_request(url):
    response = requests.get(url, verify=False)
    
    if response.status_code != 200:
        raise Exception(f"Falha ao acessar {url}")
    
    sleep(DELAY_BETWEEN_REQUESTS)
    
    return response
