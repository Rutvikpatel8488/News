from django.urls import path

from . import views
from .views import NewsListView, SportsListView, EconomyListView, PoliticsListView, LifestyleListView, \
    EntertainmentListView, AutomobileListView, DisasterListView, TopListView

urlpatterns = [
    path('scrape/', views.scrape, name="scrape"),
    path('scrape1/', views.scrape1, name="scrape1"),
    path('scrape2/', views.scrape2, name="scrape2"),
    path('scrape3/', views.scrape3, name="scrape3"),
    path('scrape4/', views.scrape4, name="scrape4"),
    path('scrape5/', views.scrape5, name="scrape5"),
    path('scrape6/', views.scrape6, name="scrape6"),
    path('scrape7/', views.scrape7, name="scrape7"),
    path('scrape8', views.scrape8, name="scrape8"),
    path('getnews/', NewsListView.as_view(), name='home'),
    path('geteconomynews/', EconomyListView.as_view(), name='economy_home'),
    path('getsportsnews/', SportsListView.as_view(), name='sports_home'),
    path('getpoliticsnews/', PoliticsListView.as_view(), name='politics_home'),
    path('getlifestylenews/', LifestyleListView.as_view(), name='lifestyle_home'),
    path('getentertainmentnews/', EntertainmentListView.as_view(), name='entertainment_home'),
    path('getautomobilenews/', AutomobileListView.as_view(), name='automobile_home'),
    path('getdisastersnews/', DisasterListView.as_view(), name='disaster_home'),
    path('gettopnews/', TopListView.as_view(), name="top_home"),
    path('menu/', views.menu_list, name='menu'),
    path('', views.home1, name="starter"),
]
