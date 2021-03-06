from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rango import views


urlpatterns = [
    url(r'^', include('rango.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
