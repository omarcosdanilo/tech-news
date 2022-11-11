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
    news = find_news()

    news_categories = {}

    for item in news:
        if item["category"] not in news_categories:
            news_categories[item["category"]] = 1
        else:
            news_categories[item["category"]] += 1

    top_categories = sorted(
        news_categories.items(), key=lambda x: (-x[1], x[0])
    )

    return [category[0] for category in top_categories]
