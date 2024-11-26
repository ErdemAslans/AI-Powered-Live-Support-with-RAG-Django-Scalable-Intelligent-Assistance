from django.contrib import admin
from django.urls import path, include
from Menu.views import home_view, ana_sayfa, gradio_interface
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home_view'),
    path('anasayfa/', ana_sayfa, name='ana_sayfa'),
    path('gradio/', gradio_interface, name='gradio_interface'),
    path('admin/', admin.site.urls),
    path('user/', include('User_Profile.urls', namespace='user_profile')),
    path('reviews/', include('Reviews.urls', namespace='reviews')),
    path('blog/',include('Blog.urls',namespace= 'blog')),
    path('rezervasyon/', include('Rezervasyon.urls', namespace='rezervasyon')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
