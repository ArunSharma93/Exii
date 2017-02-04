from django.conf.urls import url
from rango import views


urlpatterns = [
    #url(r'^$', views.index.as_view()),
    url(r'^rango/$', views.index),
    url(r'^about/$', views.about),
]
