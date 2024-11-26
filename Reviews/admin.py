from django.contrib import admin
from .models import Category, Food,Cart,CartItem,Delivery,Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'created_at', 'updated_at')
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'price', 'is_active', 'created_at', 'updated_at')
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at',)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'food',)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','food_item','date_ordered','rating','allergies')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Order,OrderAdmin)