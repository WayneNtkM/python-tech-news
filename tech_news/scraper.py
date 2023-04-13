import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url,
                                headers={"user-agent": "Fake user-agent"},
                                timeout=3)

        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


def scrape_updates(html_content):
    selector = Selector(html_content)
    return selector.css("h2.entry-title > a::attr(href)").getall()


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


def scrape_news(html_content):
    """Seu código deve vir aqui"""


def get_tech_news(amount):
    """Seu código deve vir aqui"""
