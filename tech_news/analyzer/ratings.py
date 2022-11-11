from tech_news.database import find_news


# Requisito 10.
def top_5_news():
    news = find_news()
    sorted_by_comments_count = sorted(
        news, key=lambda x: x["comments_count"], reverse=True
    )

    return [
        (content["title"], content["url"])
        for content in sorted_by_comments_count
    ][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
