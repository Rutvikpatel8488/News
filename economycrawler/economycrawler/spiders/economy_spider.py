import scrapy

from ..items import EconomycrawlerItem


class EconomySpider(scrapy.Spider):
    name = "economy"
    start_urls = [
        'https://economictimes.indiatimes.com/markets/stocks/news'
    ]

    def parse(self, response):
        div_all_news = response.xpath("//div[@class='eachStory']")
        i = 0
        for some in div_all_news:
            items = EconomycrawlerItem()
            title = some.xpath("//h3/a/meta/@content")[i].extract()
            link = "https://economictimes.indiatimes.com" + some.xpath("//h3/a/@href")[i].extract()
            img = some.xpath("//a/span[@class='imgContainer']/img/@data-original")[i].extract()
            i += 1
            items["title"] = title
            items["image"] = img
            items["url"] = link
            items['source'] = 'Economic Times'
            yield items


class ExpressSpider(scrapy.Spider):
    name = "express"
    start_urls = [
        'https://www.foxnews.com/category/us/economy'
    ]

    def parse(self, response):
        # div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")

        for i in range(12):
            items = EconomycrawlerItem()
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
