import json
from services.sitemap_service import get_motorola_links_from_sitemap
from services.phone_service import scrape_phone_data
from config.settings import SITEMAP_URL, OUTPUT_FILE
import os


def main():
    print("Obtendo links...")
    motorola_links = get_motorola_links_from_sitemap(SITEMAP_URL)

    all_phones_data = []
    print("Iniciando raspagem...")
    for link in motorola_links:
        print(f"Raspando dados da página: {link}")
        try:
            phone_data = scrape_phone_data(link)
            all_phones_data.append(phone_data)
            if not os.path.exists(OUTPUT_FILE):
                with open(OUTPUT_FILE, "w") as f:
                    pass

            with open(OUTPUT_FILE, "w") as outfile:
                json.dump(all_phones_data, outfile, indent=4)
        except Exception as e:
            print(f"Erro ao raspar a página {link}: {e}")

    print(f"Raspagem concluída.")


if __name__ == "__main__":
    main()
