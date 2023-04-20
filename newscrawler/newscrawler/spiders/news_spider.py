import scrapy

from ..items import NewscrawlerItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = [
        'https://gizmodo.com/tech/news'
    ]

    def parse(self, response):
        div_all_news = response.xpath(
            "//div[@class='sc-101yw2y-9']/div[@class='sc-11qwj9y-1 iSAYTF']/div/div")
        i = 0
        for some in div_all_news:
            items = NewscrawlerItem()
            title = some.xpath(
                "//div[@class='sc-cw4lnv-0 ksZQxB js_post_item']/div[@class='sc-cw4lnv-13 hHSpAQ']/div[@class='sc-cw4lnv-5 dYIPCV']/h2/a/text()")[
                i].extract()
            title = title[5:]
            title = title[:-3]
            link = some.xpath(
                "//div[@class='sc-cw4lnv-0 ksZQxB js_post_item']/div[@class='sc-cw4lnv-13 hHSpAQ']/div[@class='sc-cw4lnv-5 dYIPCV']/h2/a/@href")[
                i].extract()
            img = some.xpath("//div[@class='sc-cw4lnv-13 hHSpAQ']/figure/a/img/@src")[i].extract()
            i += 1
            items['title'] = title
            items['image'] = img
            items['url'] = link
            items['source'] = 'Gizmodo'
            yield items
    # if i==12:
    #	break


# class TechSpider(scrapy.Spider):
#     name = 'technews'
#     start_urls = [
#         'https://www.theverge.com/tech'
#     ]
#
#     def parse(self, response):
#
#         div_all_news = response.xpath("//div[@class='c-compact-river']/div/div")
#         i = 0
#         for some in div_all_news:
#             items = NewscrawlerItem()
#             title = some.xpath("//div/h2/a/text()")[i].extract()
#             link = some.xpath("//div/h2/a/@href")[i].extract()
#             s = some.xpath("//a/div/noscript")[i].extract()
#             l = s.split('"')
#             img = l[3]
#             i += 1
#             l = []
#             items['title'] = title
#             items['image'] = img
#             items['url'] = link
#             items['source'] = 'The Verge'
#             yield items
#             if i == 12:
#                 break

class TechSpider(scrapy.Spider):
    name = 'technews'
    start_urls = [
        'https://www.foxnews.com/tech'
    ]

    def parse(self, response):
        # div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")

        for i in range(12):
            items = NewscrawlerItem()
            title = \
                response.xpath("//div[@class='content article-list']/article/div[@class='info']/header/h4/a/text()")[
                    i].extract()
            link = 'https://www.foxnews.com' + \
                   response.xpath("//div[@class='content article-list']/article/div[@class='m']/a/@href")[i].extract()
            img = img = response.xpath("//div[@class='content article-list']/article/div[@class='m']/a/img/@src")[
                i].extract()
            items["title"] = title
            items["image"] = img
            items["url"] = link
            items['source'] = 'Fox News'
            yield items
