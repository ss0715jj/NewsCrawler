from bs4 import BeautifulSoup

def parser_news(html):
    soup = BeautifulSoup(html, 'html.parser')
    articles = []

    for item in soup.select('.left_cont .news_box .newsPost'):
        thumbnail = item.select_one(".assetThumb img").attrs['data-src']
        title = item.select_one(".assetText h3").text
        content = item.select_one(".assetText p").text

        articles.append({
            "title": title.strip(),
            "content": content.strip(),
            "thumbnail": thumbnail,
        })

    return articles