from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    try:
        finded_news = find_news()
        categories = [news["category"] for news in finded_news]
        categories_most_common = Counter(sorted(categories)).most_common(5)

        return [category[0] for category in categories_most_common]

    except ValueError:
        return []
