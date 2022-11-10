import time
from parsel import Selector
import requests


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3, headers=headers)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)

    urls = selector.css(".entry-title a::attr(href)").getall()

    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    next_page_link = selector.css(".next::attr(href)").get()

    if next_page_link:
        return next_page_link
    return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = ''.join(selector.css("h1.entry-title::text").get()).strip()
    date = selector.css("li.meta-date::text").get()
    writer = selector.css("li.meta-author a::text").get()
    comments_unformated = selector.css(".post-comments h5::text").get()
    comments = int(comments_unformated[4:5]) if comments_unformated else 0
    summary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    tags = selector.css(".post-tags ul li a::text").getall()
    category = selector.css(".meta-category span.label::text").get()

    return {
            "url": url,
            "title": title,
            "timestamp": date,
            "writer": writer,
            "comments_count": comments,
            "summary": summary,
            "tags": tags,
            "category": category,
        }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
