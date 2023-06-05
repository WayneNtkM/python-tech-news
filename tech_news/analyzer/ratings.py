from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    news = find_news()

    ratings = Counter(d["category"] for d in news)

    sorted_ratings = sorted(ratings.items(), key=lambda x: (-x[1], x[0]))

    return [i[0] for i in sorted_ratings[:5]]
