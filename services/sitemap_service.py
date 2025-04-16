from utils.request_helper import make_request
from utils.parser import parse_sitemap

def get_motorola_links_from_sitemap(sitemap_url):
    response = make_request(sitemap_url)
    motorola_links = parse_sitemap(response.content)
    return motorola_links
