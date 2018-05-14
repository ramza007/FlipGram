'''
main routes
'''
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.logout, {"next_page": '/accounts/login'}),
    url(r'^',include('gram.urls'))
]
