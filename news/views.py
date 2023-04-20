import time

from crochet import setup
from django.shortcuts import render, redirect
from uuid import uuid4
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from news.models import Headline, EHeadline, SHeadline, PHeadline, LHeadline, ENHeadline, AHeadline, DHeadline, THeadline
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.conf import settings as django_settings

# for scrapy
import os
import requests
import sys

path = django_settings.BASE_DIR
sys.path.append(path + "/newscrawler")
sys.path.append(path + "/economycrawler")
sys.path.append(path + "/sportscrawler")
sys.path.append(path + "/politicscrawler")
sys.path.append(path + "/lifestylecrawler")
sys.path.append(path + "/entertainmentcrawler")
sys.path.append(path + "/automobilecrawler")
sys.path.append(path + "/disastercrawler")
sys.path.append(path + "/topcrawler/")

# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/newscrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/sportscrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/politicscrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/economycrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/lifestylecrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/entertainmentcrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/automobilecrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/disastercrawler")
# sys.path.append("C:/Users/admin/Desktop/DJANGO/Practice_Django/News_Aggregator/topcrawler")

from newscrawler.spiders import news_spider
from economycrawler.spiders import economy_spider
from sportscrawler.spiders import sports_spider
from politicscrawler.spiders import politics_spider
from lifestylecrawler.spiders import lifestyle_spider
from entertainmentcrawler.spiders import entertainment_spider
from automobilecrawler.spiders import automobile_spider
from disastercrawler.spiders import disaster_spider
from topcrawler.spiders import top_spider
from scrapy.crawler import Crawler, CrawlerRunner
from scrapy.settings import Settings
from newscrawler import settings as my_settings
from economycrawler import settings as economy_settings
from sportscrawler import settings as sports_settings
from politicscrawler import settings as politics_settings
from lifestylecrawler import settings as lifestyle_settings
from entertainmentcrawler import settings as entertainment_settings
from automobilecrawler import settings as automobile_settings
from disastercrawler import settings as disaster_settings
from topcrawler import settings as top_settings
from scrapy.utils.log import configure_logging


# scrapyd = ScrapydAPI('http://localhost:6800')

def home1(request):
    return render(request, "news/index.html")


'''
@login_required
def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context ={
            'object_list' : headlines,
    }
    return render(request, "news/home.html", context)
'''


class NewsListView(ListView):
    model = Headline
    template_name = 'news/home.html'
    paginate_by = 5


'''
@login_required
def economy_news_list(request):
    headlines = EHeadline.objects.all()[::-1]
    context ={
            'object_list' : headlines,
    }
    return render(request, "news/economy_home.html", context)
'''


class EconomyListView(ListView):
    model = EHeadline
    template_name = 'news/economy_home.html'
    paginate_by = 5


'''
@login_required
def sports_news_list(request):
    headlines = SHeadline.objects.all()[::-1]
    context ={
            'object_list' : headlines,
    }
    return render(request, "news/sports_home.html", context)
'''


class SportsListView(ListView):
    model = SHeadline
    template_name = 'news/sports_home.html'
    paginate_by = 5


class PoliticsListView(ListView):
    model = PHeadline
    template_name = 'news/politics_home.html'
    paginate_by = 5


class LifestyleListView(ListView):
    model = LHeadline
    template_name = 'news/lifestyle_home.html'
    paginate_by = 5


class EntertainmentListView(ListView):
    model = ENHeadline
    template_name = 'news/entertainment_home.html'
    paginate_by = 5


class AutomobileListView(ListView):
    model = AHeadline
    template_name = 'news/automobile_home.html'
    paginate_by = 5


class DisasterListView(ListView):
    model = DHeadline
    template_name = 'news/disaster_home.html'
    paginate_by = 5

class TopListView(ListView):
    model = THeadline
    template_name = 'news/top_home.html'
    paginate_by = 5


@login_required
def menu_list(request):
    return render(request, "news/topics_list.html")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape(request):
    Headline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(my_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(news_spider.NewsSpider)
    time.sleep(3)
    d = runner.crawl(news_spider.TechSpider)
    time.sleep(3)
    return redirect("../getnews/")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape1(request):
    EHeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(economy_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(economy_spider.EconomySpider)
    time.sleep(3)
    d = runner.crawl(economy_spider.ExpressSpider)
    time.sleep(3)
    return redirect("../geteconomynews/")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape2(request):
    SHeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(sports_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(sports_spider.SportsSpider)
    time.sleep(3)
    d = runner.crawl(sports_spider.HtimesSpider)
    time.sleep(3)
    return redirect("../getsportsnews/")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape3(request):
    PHeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(politics_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(politics_spider.PoliticsSpider)
    time.sleep(3)
    d = runner.crawl(politics_spider.EconomicSpider)
    time.sleep(3)
    return redirect("../getpoliticsnews/")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape4(request):
    LHeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(lifestyle_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(lifestyle_spider.LifestyleSpider)
    time.sleep(3)
    d = runner.crawl(lifestyle_spider.HealthSpider)
    time.sleep(3)
    return redirect("../getlifestylenews/")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape5(request):
    ENHeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(entertainment_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(entertainment_spider.EntertainmentSpider)
    time.sleep(3)
    d = runner.crawl(entertainment_spider.EntrtnmentSpider)
    time.sleep(3)
    return redirect("../getentertainmentnews/")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape6(request):
    AHeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(automobile_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(automobile_spider.AutomobileSpider)
    time.sleep(3)
    d = runner.crawl(automobile_spider.AutoSpider)
    time.sleep(3)
    return redirect("../getautomobilenews/")


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape7(request):
    DHeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(disaster_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(disaster_spider.DisastersSpider)
    time.sleep(3)
    d = runner.crawl(disaster_spider.DisasterSpider)
    time.sleep(3)
    return redirect("../getdisastersnews/")

@csrf_exempt
@require_http_methods(['POST', 'GET'])
def scrape8(request):
    THeadline.objects.all().delete()
    crawler_settings = Settings()

    setup()
    configure_logging()
    crawler_settings.setmodule(disaster_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    d = runner.crawl(top_spider.TopSpider)
    time.sleep(3)
    return redirect("../gettopnews/")