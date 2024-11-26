import json
from django.contrib.auth.models import User
from Reviews import  Category, Food, Cart, Delivery, Order
from Blog import BlogModel
from Rezervasyon import Rezervasyon

import os
import django

# Django settings dosyasını belirtin
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
# JSON dosyasını aç
with open('data.json', 'r') as file:
    data = json.load(file)

# Categories
for category_data in data['categories']:
    Category.objects.create(
        title=category_data['title'],
        slug=category_data['slug'],
        is_active=category_data['is_active'],
        created_at=category_data['created_at'],
        updated_at=category_data['updated_at']
    )

# Foods
for food_data in data['foods']:
    category = Category.objects.get(id=food_data['category_id'])
    user = User.objects.get(id=food_data['user_id'])
    Food.objects.create(
        title=food_data['title'],
        slug=food_data['slug'],
        is_active=food_data['is_active'],
        created_at=food_data['created_at'],
        updated_at=food_data['updated_at'],
        user=user,
        category=category,
        cover_image=food_data['cover_image'],
        description=food_data['description'],
        price=food_data['price'],
        view_count=food_data['view_count'],
        allergens=food_data.get('allergens', None)
    )

# Rezervasyonlar
for rezervasyon_data in data['reservations']:
    user = User.objects.get(id=rezervasyon_data['user_id'])
    Rezervasyon.objects.create(
        user=user,
        table_number=rezervasyon_data['table_number'],
        reservation_time=rezervasyon_data['reservation_time'],
        phone_number=rezervasyon_data['phone_number'],
        is_active=rezervasyon_data['is_active'],
        created_at=rezervasyon_data['created_at'],
        updated_at=rezervasyon_data['updated_at']
    )

# Blog Modelleri
for blog_data in data['blog_models']:
    author = User.objects.get(id=blog_data['author_id'])
    BlogModel.objects.create(
        author=author,
        slug=blog_data['slug'],
        title=blog_data['title'],
        cover_image=blog_data['cover_image'],
        description=blog_data['description'],
        description2=blog_data['description2'],
        is_active=blog_data['is_active'],
        created_at=blog_data['created_at'],
        updated_at=blog_data['updated_at']
    )

# Cart
for cart_data in data['cart']:
    user = User.objects.get(id=cart_data['user_id'])
    Cart.objects.create(
        user=user,
        created_at=cart_data['created_at']
    )

# Delivery
for delivery_data in data['delivery']:
    user = User.objects.get(id=delivery_data['user_id']) if delivery_data['user_id'] else None
    Delivery.objects.create(
        user=user,
        status=delivery_data['status'],
        created_at=delivery_data['created_at'],
        updated_at=delivery_data['updated_at']
    )

# Orders
for order_data in data['order']:
    user = User.objects.get(id=order_data['user_id'])
    Order.objects.create(
        user=user,
        food_item=order_data['food_item'],
        date_ordered=order_data['date_ordered'],
        rating=order_data['rating'],
        allergies=order_data['allergies']
    )