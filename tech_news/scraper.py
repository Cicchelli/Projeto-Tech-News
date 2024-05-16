import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url, headers=None, timeout=3):
    if headers is None:
        headers = {"user-agent": "Fake user-agent"}

    try:
        time.sleep(1)  # Simulate a delay
        response = requests.get(url, headers=headers, timeout=timeout)

        if response.status_code != 200:
            return None
        return response.text

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_links = selector.css('.entry-title a::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
