from django.conf.urls import url
from . import views

urlpatterns=[
    url('^home',views.base,name = 'base'),
    url(r'^profile/', views.profile, name='profileView'),
    url(r'^$', views.explore, name='explore')
]
