from django.conf.urls import url
from django.urls import path, include
from .views import pagina_principal

urlpatterns = [
    path('', pagina_principal, name=''),
]