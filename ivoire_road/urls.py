from django.urls import path
from .views import home,chargement

urlpatterns = [
    path('', home, name='home'),
    path('chargement/', chargement, name='chargement'),
]