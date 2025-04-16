from bs4 import BeautifulSoup
from bs4 import Comment
import re

def parse_sitemap(response_content):
    soup = BeautifulSoup(response_content, "xml")
    links = soup.find_all("loc")
    motorola_links = [link.text for link in links if "motorola" in link.text.lower()]
    return motorola_links

def parse_phone_data(response_content):
    soup = BeautifulSoup(response_content, "html.parser")
    phone_data = {}

    # Encontrar a tabela de especificações
    datasheet_comment = soup.find(
        string=lambda text: isinstance(text, Comment)
        and "Beginning of Datasheet" in text
    )

    if datasheet_comment:
        datasheet = datasheet_comment.find_next("table")
        rows = datasheet.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 2:
                key = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                phone_data[key] = value
    else:
        raise Exception("Datasheet não encontrado na página")

    # Procurar a primeira div com a classe 'sidebar' e capturar a imagem dentro dela
    sidebar = soup.find("div", class_="sidebar")
    if sidebar:
        img_tag = sidebar.find("img")
        if img_tag and "src" in img_tag.attrs:
            phone_data["imageSrc"] = img_tag["src"]
        else:
            phone_data["imageSrc"] = None
    else:
        phone_data["imageSrc"] = None
        print("não encontrado")

    return phone_data
