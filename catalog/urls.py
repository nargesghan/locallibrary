from django.urls import path,re_path
from . import views

app_name='catalog'
urlpatterns=[
    re_path(r'^$',views.index,name='index'),
]