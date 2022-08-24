import requests
import time
import parsel


# Requisito 1
def fetch(url, timeout=3):
    try:
        response = requests.get(
            url,
            timeout=timeout,
            header={"user-agent": "Fake user-agent"},
        )
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return requests.get(url).text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    urls_news = selector.css("h2.entry-title a::attr(href)").getall()
    return urls_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    if not next_page_link:
        return None
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    dict_news = {}

    dict_news["url"] = selector.xpath("//link[@rel='canonical']/@href").get()
    title = selector.css("h1.entry-title ::text").get()
    dict_news["title"] = title.strip()
    dict_news["timestamp"] = selector.css(".meta-date::text").get()
    dict_news["writer"] = selector.css("span.author .url.fn.n::text").get()
    comments = selector.css(".post-comments.post-comments-simple").getall()
    dict_news["comments_count"] = len(comments)
    summary = selector.xpath("string(.//div[@class='entry-content']/p)").get()
    dict_news["summary"] = summary.strip()
    dict_news["tags"] = selector.css(".post-tags ul li a::text").getall()
    dict_news["category"] = selector.css(".label::text").get()

    # news = {
    #     "url": url,
    #     "title": title.strip(),
    #     "timestamp": timestamp,
    #     "writer": writer,
    #     "comments_count": comments_count,
    #     "summary": summary.strip(),
    #     "tags": tags,
    #     "category": category,
    # }
    return dict_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
