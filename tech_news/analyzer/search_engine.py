from datetime import datetime
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
    list = []
    try:
        usa_date = datetime.strptime(date, "%Y-%m-%d")
        br_date = datetime.strftime(usa_date, "%d/%m/%Y")
        all_news = search_news({"timestamp": br_date})
        for new in all_news:
            list.append((new["title"], new["url"]))
        return list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    tags = search_news({"tags": {"$regex": tag, "$options": "i"}})
    data = []

    for new in tags:
        data.append((new["title"], new["url"]))
    return data


# Requisito 9
def search_by_category(category):
    data = search_news({"category": {"$regex": category, "$options": "i"}})
    list = []
    for new in data:
        list.append((new["title"], new["url"]))
    return list
