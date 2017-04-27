from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^mfuzz$', views.mfuzzHome, name='mfuzz'),
    url(r'^mfuzz/(?P<mfuzz_nb>[0-9]+)$', views.mfuzzResults, name='mfuzzResults'),
    url(r'^results$', views.results, name='results'),
    url(r'^search$', views.searchResults, name='search'),
    url(r'^search/(?P<search_query>\w+)$', views.searchResults, name='search'),
    url(r'^test$', views.test, name='test'),
]