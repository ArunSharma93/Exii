from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rango import views


urlpatterns = [
    url(r'^', include('rango.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]


if settings
