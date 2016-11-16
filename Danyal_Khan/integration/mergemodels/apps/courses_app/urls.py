from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^courses_app/add$', views.add, name='my_add'),
    url(r'^courses_app/destroy/(?P<id>\d+)$', views.destroy, name= 'my_delete'),
    url(r'^courses_app/remove/(?P<id>\d+)$', views.remove, name= 'my_remove'),
    url(r'^courses_app/admin$', views.admin, name= 'admin'),
    url(r'^courses_app/create$', views.create, name= 'create')
    
]