from django.conf.urls import patterns, url

from companiesEvaluator import views

urlpatterns = patterns('', 
   url(r'^$', views.index, name='index'),
   url(r'^ranking', views.ranking, name='ranking'),
   url(r'^compare', views.compare, name='compare'),
   url(r'^comofunciona', views.comofunciona, name='comofunciona'),
   url(r'^procon', views.procon, name='procon'),
   url(r'^charts', views.charts, name='charts')
)
