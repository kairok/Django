from django.conf.urls import url, include
from django.contrib import admin
# from . import views
from website.views import home, dashboard, webapp, geo, test, region, quick, channel, monitoring, region2, manual

# from website.fusioncharts import a_2D_Bar_Chart

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^webapp/$', webapp, name='webapp'),
    url(r'^settings/$', webapp, name='settings'),
    url(r'^geo/$', geo, name='geo'),
    url(r'^test/$', test, name='test'),
    url(r'^region/$', region, name='region'),
    url(r'^quick/$', quick, name='quick'),
    url(r'^channel/$', channel, name='channel'),
    url(r'^monitoring/', monitoring, name='monitoring'),
#url(r'^monitoring/(?P<slug>\w+)', monitoring, name='monitoring'),
    url(r'^region2/$', region2, name='region2'),
    url(r'^manual/$', manual, name='manual')
    # url(r'^render-bar2d/', a_2D_Bar_Chart.chart, name='chart')
    # url(r'^test/home/$', home, name='home')
]