from django.urls import path
from .views import create_rezervasyon, rezervasyon_list

app_name = 'rezervasyon'

urlpatterns = [
    path('create/', create_rezervasyon, name='create_rezervasyon'),
    path('rezervasyon_list/', rezervasyon_list, name='rezervasyon_list'),
]