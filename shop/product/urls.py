
from django.urls import path
from .views import Home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)