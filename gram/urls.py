from django.conf.urls import url, include
from . import views

urlpatterns=[
    url('^home',views.base,name = 'base'),
    url(r'^profile/', views.profile, name='profileView'),
    url(r'^$', views.explore, name='explore'),
    url(r'^timeline', views.timeline, name='timeline'),
    url(r'^accounts/', include('registration.backends.simple.urls'))
]
