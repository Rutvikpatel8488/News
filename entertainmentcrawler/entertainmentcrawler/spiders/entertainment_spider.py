import scrapy

from ..items import EntertainmentcrawlerItem


class EntertainmentSpider(scrapy.Spider):
    name = "entertainment"
    start_urls = [
        'https://timesofindia.indiatimes.com/briefs/entertainment'
    ]

    def parse(self, response):
        for i in range(13):
            items = EntertainmentcrawlerItem()
            title = response.xpath("//div[@class='briefs_outer clearfix']/div[@class='brief_box']/h2/a/text()")[i].extract()
            link = response.xpath("//div[@class='briefs_outer clearfix']/div[@class='brief_box']/a/@href")[i].extract()
            img = response.xpath("//div[@class='briefs_outer clearfix']/div[@class='brief_box']/a/img/@data-src")[i].extract()
            items["title"] = title
            items["image"] = img
            items["url"] = link
            items['source'] = 'Indian Express'
            yield items


class EntrtnmentSpider(scrapy.Spider):
    name = "entrtnment"
    start_urls = [
         'https://www.foxnews.com/entertainment'
    ]

    def parse(self, response):
        # div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")

        for i in range(12):
            items = EntertainmentcrawlerItem()
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

