from utils.request_helper import make_request
from utils.parser import parse_phone_data

def scrape_phone_data(url):
    response = make_request(url)
    phone_data = parse_phone_data(response.content)
    return phone_data
