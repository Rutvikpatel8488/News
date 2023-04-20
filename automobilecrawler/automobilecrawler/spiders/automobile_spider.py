from ..items import AutomobilecrawlerItem
import scrapy


class AutomobileSpider(scrapy.Spider):
    name = "automobile"
    start_urls = [
        'https://www.autonews.com/'
    ]

    def parse(self, response):
        # div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")
        for i in range(10):
            items = AutomobilecrawlerItem()
            title = response.xpath("//div[@class='region region-content']/div[@class='region-featured row']/a/text()")[
                i].extract()
            link = "https://www.autonews.com" + response.xpath("//h3/a/@href")[i].extract()
            img = response.xpath("//a/picture[@class='lazyloaded']/img/@data-original")[i].extract()
            i += 1
            items["title"] = title
            items["image"] = img
            items["url"] = link
            items['source'] = 'Automobile Times'
            yield items


class AutoSpider(scrapy.Spider):
    name = "express"
    start_urls = [
        'https://www.foxnews.com/auto'
    ]

    def parse(self, response):
        # div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")

        for i in range(20):
            items = AutomobilecrawlerItem()
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
