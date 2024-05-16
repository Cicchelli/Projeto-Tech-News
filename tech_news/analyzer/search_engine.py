from tech_news.database import db

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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
