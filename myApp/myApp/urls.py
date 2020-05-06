from django.conf.urls import url, include
from django.contrib import admin
from FullThrottle import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^post/$', views.post, name="post"),
]
