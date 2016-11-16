from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^ninjagold/process$', views.process, name= 'process')
]
