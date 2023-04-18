from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(d["title"], d["url"]) for d in result]


def search_by_date(date):
    try:
        formated_date = datetime.strftime(
            datetime.strptime(date, "%Y-%m-%d"), "%d/%m/%Y")

        return [(d["title"], d["url"])
                for d in search_news({"timestamp": formated_date})]

    except ValueError:
        raise ValueError("Data inválida")


def search_by_category(category):
    return [(d["title"], d["url"])
            for d in search_news({"category": {"$regex": category,
                                               "$options": "i"}})]
