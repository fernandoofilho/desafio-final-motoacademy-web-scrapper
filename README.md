# MotoDevice WebScraper

Web Scraper desenvolvido como parte do projeto final do **Moto Academy 2.0**, promovido pelo **Instituto de Pesquisas Eldorado**.

Este módulo tem como objetivo coletar dados de dispositivos **Motorola** diretamente do site [phonedb.net], estruturando e armazenando essas informações em formato JSON, posteriormente inseridas em um banco MongoDB utilizado pela API MotoDevice.

---

## 🔍 Visão Geral

Devido à ausência de APIs públicas confiáveis e com dados detalhados, desenvolvemos um scraper customizado capaz de:

- Identificar URLs relevantes de dispositivos Motorola
- Coletar dados técnicos (especificações, imagens, reviews)
- Ignorar conteúdos irrelevantes como anúncios ou logotipos
- Processar imagens em diferentes formatos (.jpg, .png, etc)
- Exportar os dados em formato JSON compatível com MongoDB

---

## 🛠️ Como Funciona

1. **Descoberta de URLs**  
   Utiliza as diretivas do `robots.txt` para descobrir páginas de dispositivos.

2. **Extração de Dados**  
   Acessa cada página de dispositivo, analisa a estrutura HTML e extrai informações como:
   - Nome do modelo
   - Imagens do dispositivo
   - Ficha técnica
   - Links de reviews

3. **Tratamento de Imagens**  
   Utiliza expressões regulares (Regex) para identificar imagens relevantes, descartando banners e logotipos.

4. **Exportação de Dados**  
   Os dados extraídos são formatados em JSON e prontos para alimentar o banco MongoDB utilizado pela API.

---

## 🚀 Tecnologias Utilizadas

- Python
- BeautifulSoup
- Requests
- Regex
- JSON
---

## 📦 Execução

```bash
pip install -r requirements.txt
python scraper.py
```

> ⚠️ A execução pode demorar dependendo da quantidade de dispositivos disponíveis.

---

## 📁 Saída Esperada

Os arquivos `.json` com os dados estruturados serão salvos na pasta `output/`. Este arquivo pode ser utilizado para popular a base de dados.

---

## 📜 Licença

Este scraper foi desenvolvido exclusivamente para fins acadêmicos e de pesquisa. Uso pessoal permitido.
