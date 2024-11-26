import json

import os
import django

# Django settings dosyasını belirtin
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
# JSON dosyasını aç
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Reviews.models import Category, Food, Cart, Delivery, Order
from Blog.models import BlogModel
from Rezervasyon.models import Rezervasyon


with open('data.json', 'r') as file:
    data = json.load(file)

class Command(BaseCommand):
    help = 'Load data from JSON files into the database'

    def handle(self, *args, **options):
        # Categories
        with open('categories.json', 'r', encoding='utf-8') as file:
            categories_data = json.load(file)
            for category_data in categories_data['categories']:
                Category.objects.create(
                    title=category_data['title'],
                    slug=category_data['slug'],
                    is_active=category_data['is_active'],
                    created_at=category_data['created_at'],
                    updated_at=category_data['updated_at'],
                )

        # Foods
        with open('food.json', 'r', encoding='utf-8') as file:
            foods_data = json.load(file)
            for food_data in foods_data['foods']:
                category = Category.objects.get(id=food_data['category_id'])
                Food.objects.create(
                    title=food_data['title'],
                    slug=food_data['slug'],
                    is_active=food_data['is_active'],
                    created_at=food_data['created_at'],
                    updated_at=food_data['updated_at'],
                    user_id=food_data['user_id'],  # Assuming user_id is correct
                    category=category,
                    cover_image=food_data['cover_image'],
                    description=food_data['description'],
                    price=food_data['price'],
                    view_count=food_data['view_count'],
                    allergens=food_data['allergens'],
                )

        # Cart
        with open('cart.json', 'r', encoding='utf-8') as file:
            cart_data = json.load(file)
            for cart in cart_data['cart']:
                Cart.objects.create(
                    user_id=cart['user_id'],
                    created_at=cart['created_at'],
                )

        # Delivery
        with open('delivery.json', 'r', encoding='utf-8') as file:
            delivery_data = json.load(file)
            for delivery in delivery_data['delivery']:
                Delivery.objects.create(
                    user_id=delivery['user_id'],
                    status=delivery['status'],
                    created_at=delivery['created_at'],
                    updated_at=delivery['updated_at'],
                )

        # Order
        with open('order.json', 'r', encoding='utf-8') as file:
            order_data = json.load(file)
            for order in order_data['order']:
                Order.objects.create(
                    user_id=order['user_id'],
                    food_item=order['food_item'],
                    date_ordered=order['date_ordered'],
                    rating=order['rating'],
                    allergies=order['allergies'],
                )

        # Blog Models
        with open('blog.json', 'r', encoding='utf-8') as file:
            blog_data = json.load(file)
            for blog in blog_data['blog_models']:
                BlogModel.objects.create(
                    author_id=blog['author_id'],
                    slug=blog['slug'],
                    title=blog['title'],
                    cover_image=blog['cover_image'],
                    description=blog['description'],
                    description2=blog['description2'],
                    is_active=blog['is_active'],
                    created_at=blog['created_at'],
                    updated_at=blog['updated_at'],
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))