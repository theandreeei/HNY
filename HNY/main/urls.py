from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('card/<str:name>', views.card)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
