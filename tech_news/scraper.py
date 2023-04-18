import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)
    return selector.css("span.current ~ a.page-numbers::attr(href)").get()


def scrape_news(html_content):
    selector = Selector(html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get().strip(),
        "writer": selector.css(".author > a::text").get(),
        "reading_time": int(selector.css(".meta-reading-time::text").get()
                            .split(" ")[0]),
        "summary": "".join(selector.css(
                                    ".entry-content > p:nth-of-type(1) *::text"
                                    ).getall()).strip(),
        "category": selector.css("span.label::text").get(),
    }


def get_tech_news(amount):
    BASE_URL = "https://blog.betrybe.com"
    news = []
    counter = 0

    while counter < amount:
        response = fetch(BASE_URL)
        news_urls = scrape_updates(response)

        for url in news_urls:
            news.append(scrape_news(fetch(url)))
            counter += 1
            if counter == amount:
                break
        BASE_URL = scrape_next_page_link(response)
    create_news(news)
    return news
