from tech_news.database import db
from datetime import datetime

# Requisito 7
def search_by_title(title):
    # Use list comprehension for brevity
    news_results = [(n['title'], n['url']) for n in db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {'title': True, 'url': True, '_id': False}
    )]
    return news_results


# Requisito 8
def search_by_date(date):
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news_date = db.news.find(
        {"timestamp": datetime.strftime(format_date, "%d/%m/%Y")},
        {"title": True, "url": True, "_id": False},
    )

    news_return = [(n["title"], n["url"]) for n in news_date]
    return news_return


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
