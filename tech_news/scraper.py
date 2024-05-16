import time
import requests
from parsel import Selector
import parsel


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
    selector = Selector(html_content)
    scrape_next_page_link = selector.css('.next.page-numbers::attr(href)').get()
    return scrape_next_page_link


# Requisito 4
def scrape_news(html_content):
    news_dict = {}
    selector = parsel.Selector(text=html_content)

    news_dict["url"] = selector.css("head link[rel=canonical]::attr(href)").get()
    news_dict["title"] = selector.css(".entry-title::text").get().strip(" \xa0")
    news_dict["timestamp"] = selector.css(".meta-date::text").get()
    news_dict["writer"] = selector.css(".author a::text").get()

    # Extracting reading time as an integer
    news_dict["reading_time"] = int(selector.css(".meta-reading-time::text").re_first(r"\d+"))

    # Extracting summary from the first paragraph
    paragraph = selector.xpath("(//p)[1]//text()").getall()
    news_dict["summary"] = "".join(paragraph).strip(" \xa0")

    news_dict["category"] = selector.css(".meta-category .label::text").get()

    return news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
