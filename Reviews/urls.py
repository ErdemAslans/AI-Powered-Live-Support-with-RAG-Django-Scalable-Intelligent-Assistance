from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reviews' 

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-to-cart/<int:food_id>//', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:food_slug>/', views.food_detail, name='food_detail'),
    path('delivery-status/', views.delivery_status, name='delivery_status'),
    path('delivery/',views.delivery,name='delivery'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
