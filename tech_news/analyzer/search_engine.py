from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    data = []

    for new in news:
        data.append((new["title"], new["url"]))
    return data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    tags = search_news({"tags": {"$regex": tag, "$options": "i"}})
    data = []

    for new in tags:
        data.append((new["title"], new["url"]))
    return data


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
