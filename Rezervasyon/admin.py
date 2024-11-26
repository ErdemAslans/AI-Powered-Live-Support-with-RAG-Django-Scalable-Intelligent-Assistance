from django.contrib import admin
from .models import Rezervasyon

class RezervasyonAdmin(admin.ModelAdmin):
    list_display = ('user','table_number','reservation_time','phone_number','is_active', 'created_at', 'updated_at')

admin.site.register(Rezervasyon, RezervasyonAdmin)