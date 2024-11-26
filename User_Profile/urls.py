from django.urls import path
from User_Profile.views import login_view,logout_view,register_view
from django.conf import settings
from django.conf.urls.static import static
app_name = 'user_profile'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name = 'logout_view'),
    path('register/',register_view, name = 'register_view')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
