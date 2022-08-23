import requests
import time
import parsel


# Requisito 1
def fetch(url, timeout=3):
    try:
        response = requests.get(
            url,
            timeout=timeout,
            header={"user-agent": "Fake user-agent"},
        )
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return requests.get(url).text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    urls_news = selector.css("h2.entry-title a::attr(href)").getall()
    return urls_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    if not next_page_link:
        return None
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
