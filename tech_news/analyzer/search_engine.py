from tech_news.database import search_news
from datetime import date as date_obj


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": f"{title}", "$options": "i"}})

    return [(content["title"], content["url"]) for content in news]


# Requisito 7
def search_by_date(date):
    try:
        formated_date = date_obj.fromisoformat(date).strftime("%d/%m/%Y")

        news = search_news({"timestamp": formated_date})

        return [(content["title"], content["url"]) for content in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = search_news(
        {"tags": {"$elemMatch": {"$regex": f"{tag}", "$options": "i"}}}
    )
    return [(content["title"], content["url"]) for content in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
