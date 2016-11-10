from django.conf.urls import url
from  . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_form', views.submit_form),
    url(r'^result', views.result),
    url(r'^reset', views.reset)
]
