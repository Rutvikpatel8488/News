import scrapy

from ..items import SportscrawlerItem


class SportsSpider(scrapy.Spider):
    name = "sports"
    start_urls = [
        'https://indianexpress.com/section/sports/'
    ]

    def parse(self, response):
        # div_all_news = response.xpath("//div[@class='articles']")
        i = 0
        for i in range(20):
            items = SportscrawlerItem()
            title = \
                response.xpath("//div[@class='container']/div[@class='articles']/h2/a/text()")[
                    i].extract()
            link = 'https://indianexpress.com/section/sports/' + \
                   response.xpath("//div[@class='container']/div[@class='articles']/div[@class='snap']/a/@href")[i].extract()
            img = img = response.xpath("//div[@class='container']/div[@class='articles']/div[@class='snap']/a/img/@src")[
                i].extract()
            items["title"] = title
            items["image"] = img
            items["url"] = link
            items['source'] = 'Indian Express'
            yield items


class HtimesSpider(scrapy.Spider):
    name = "sports"
    start_urls = [
        'https://www.foxnews.com/sports'
    ]

    def parse(self, response):
        # div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")

        for i in range(12):
            items = SportscrawlerItem()
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
