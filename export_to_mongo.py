import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from pymongo import MongoClient
from Blog.models import BlogModel
from Reviews.models import Category, Food, Cart, Delivery, Order
from Rezervasyon.models import Rezervasyon
# MongoDB Bağlantısı
client = MongoClient("mongodb+srv://Faymis123:Faymis123@restorant.dmuoghs.mongodb.net/?retryWrites=true&w=majority")
db = client['Restorant']  # Veritabanı adı

# BlogModel verilerini aktarma
blogs_collection = db['blogs']
for blog in BlogModel.objects.all():
    blog_data = {
        'id': blog.id,
        'title': blog.title,
        'slug': blog.slug,
        'author_id': blog.author_id,
        'description': blog.description,
        'description2': blog.description2,
        'cover_image': blog.cover_image.name,
        'is_active': blog.is_active,
        'created_at': blog.created_at,
        'updated_at': blog.updated_at,
    }
    blogs_collection.insert_one(blog_data)

# Aynı şekilde diğer modeller için de veri aktarımı yapabilirsiniz:
# Category
categories_collection = db['categories']
for category in Category.objects.all():
    category_data = {
        'id': category.id,
        'title': category.title,
        'slug': category.slug,
        'is_active': category.is_active,
        'created_at': category.created_at,
        'updated_at': category.updated_at,
    }
    categories_collection.insert_one(category_data)

# Food
foods_collection = db['foods']
for food in Food.objects.all():
    food_data = {
        'id': food.id,
        'title': food.title,
        'slug': food.slug,
        'category_id': food.category_id,
        'user_id': food.user_id,
        'cover_image': food.cover_image.name,
        'description': food.description,
        'price': str(food.price),
        'view_count': food.view_count,
        'allergens': food.allergens,
        'is_active': food.is_active,
        'created_at': food.created_at,
        'updated_at': food.updated_at,
    }
    foods_collection.insert_one(food_data)

    # Cart
carts_collection = db['carts']
for cart in Cart.objects.all():
    cart_data = {
        'id': cart.id,
        'user_id': cart.user_id,
        'created_at': cart.created_at,
    }
    carts_collection.insert_one(cart_data)

# Delivery
deliveries_collection = db['deliveries']
for delivery in Delivery.objects.all():
    delivery_data = {
        'id': delivery.id,
        'user_id': delivery.user_id,
        'status': delivery.status,
        'created_at': delivery.created_at,
        'updated_at': delivery.updated_at,
    }
    deliveries_collection.insert_one(delivery_data)

# Order
orders_collection = db['orders']
for order in Order.objects.all():
    order_data = {
        'id': order.id,
        'user_id': order.user_id,
        'food_item': order.food_item,
        'date_ordered': order.date_ordered,
        'rating': order.rating,
        'allergies': order.allergies,
    }
    orders_collection.insert_one(order_data)

# Rezervasyon
reservations_collection = db['reservations']
for rezervasyon in Rezervasyon.objects.all():
    rezervasyon_data = {
        'id': rezervasyon.id,
        'user_id': rezervasyon.user_id,
        'table_number': rezervasyon.table_number,
        'reservation_time': rezervasyon.reservation_time,
        'phone_number': rezervasyon.phone_number,
        'is_active': rezervasyon.is_active,
        'created_at': rezervasyon.created_at,
        'updated_at': rezervasyon.updated_at,
    }
    reservations_collection.insert_one(rezervasyon_data)