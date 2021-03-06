from django.conf.urls import url, include
from rango import views


urlpatterns = [
    #url(r'^$', views.index.as_view()),
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^add_category/$', views.add_category, name = "add_category"),
    url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name = 'user_login'),
    url(r'^restricted/$', views.restricted, name = 'restricted'),
    url(r'^logout/$', views.user_logout, name = 'logout'),
              ]
