from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from Blog.models import BlogModel 
from Reviews.models import Category, Food, Cart, Delivery, Order
from Rezervasyon.models import Rezervasyon
from django.contrib.auth.models import User
from mangodb_utils import save_to_mongodb, delete_from_mongodb

# BlogModel için Signal
@receiver(post_save, sender=BlogModel)
def save_blog_to_mongodb(sender, instance, **kwargs):
    blog_data = {
        'id': instance.id,
        'title': instance.title,
        'slug': instance.slug,
        'author_id': instance.author_id,
        'description': instance.description,
        'description2': instance.description2,
        'cover_image': instance.cover_image.name,
        'is_active': instance.is_active,
        'created_at': instance.created_at,
        'updated_at': instance.updated_at,
    }
    save_to_mongodb('blogs', {'id': instance.id}, blog_data)

@receiver(post_delete, sender=BlogModel)
def delete_blog_from_mongodb(sender, instance, **kwargs):
    delete_from_mongodb('blogs', {'id': instance.id})

# Category için Signal
@receiver(post_save, sender=Category)
def save_category_to_mongodb(sender, instance, **kwargs):
    category_data = {
        'id': instance.id,
        'title': instance.title,
        'slug': instance.slug,
        'is_active': instance.is_active,
        'created_at': instance.created_at,
        'updated_at': instance.updated_at,
    }
    save_to_mongodb('categories', {'id': instance.id}, category_data)

@receiver(post_delete, sender=Category)
def delete_category_from_mongodb(sender, instance, **kwargs):
    delete_from_mongodb('categories', {'id': instance.id})

# Food için Signal
@receiver(post_save, sender=Food)
def save_food_to_mongodb(sender, instance, **kwargs):
    food_data = {
        'id': instance.id,
        'title': instance.title,
        'slug': instance.slug,
        'category_id': instance.category_id,
        'user_id': instance.user_id,
        'cover_image': instance.cover_image.name,
        'description': instance.description,
        'price': str(instance.price),
        'view_count': instance.view_count,
        'allergens': instance.allergens,
        'is_active': instance.is_active,
        'created_at': instance.created_at,
        'updated_at': instance.updated_at,
    }
    save_to_mongodb('foods', {'id': instance.id}, food_data)

@receiver(post_delete, sender=Food)
def delete_food_from_mongodb(sender, instance, **kwargs):
    delete_from_mongodb('foods', {'id': instance.id})

# Cart için Signal
@receiver(post_save, sender=Cart)
def save_cart_to_mongodb(sender, instance, **kwargs):
    cart_data = {
        'id': instance.id,
        'user_id': instance.user_id,
        'created_at': instance.created_at,
    }
    save_to_mongodb('carts', {'id': instance.id}, cart_data)

@receiver(post_delete, sender=Cart)
def delete_cart_from_mongodb(sender, instance, **kwargs):
    delete_from_mongodb('carts', {'id': instance.id})

# Delivery için Signal
@receiver(post_save, sender=Delivery)
def save_delivery_to_mongodb(sender, instance, **kwargs):
    delivery_data = {
        'id': instance.id,
        'user_id': instance.user_id,
        'status': instance.status,
        'created_at': instance.created_at,
        'updated_at': instance.updated_at,
    }
    save_to_mongodb('deliveries', {'id': instance.id}, delivery_data)

@receiver(post_delete, sender=Delivery)
def delete_delivery_from_mongodb(sender, instance, **kwargs):
    delete_from_mongodb('deliveries', {'id': instance.id})

# Order için Signal
@receiver(post_save, sender=Order)
def save_order_to_mongodb(sender, instance, **kwargs):
    order_data = {
        'id': instance.id,
        'user_id': instance.user_id,
        'food_item': instance.food_item,
        'date_ordered': instance.date_ordered,
        'rating': instance.rating,
        'allergies': instance.allergies,
    }
    save_to_mongodb('orders', {'id': instance.id}, order_data)

@receiver(post_delete, sender=Order)
def delete_order_from_mongodb(sender, instance, **kwargs):
    delete_from_mongodb('orders', {'id': instance.id})

# Rezervasyon için Signal
@receiver(post_save, sender=Rezervasyon)
def save_rezervasyon_to_mongodb(sender, instance, **kwargs):
    rezervasyon_data = {
        'id': instance.id,
        'user_id': instance.user_id,
        'table_number': instance.table_number,
        'reservation_time': instance.reservation_time,
        'phone_number': instance.phone_number,
        'is_active': instance.is_active,
        'created_at': instance.created_at,
        'updated_at': instance.updated_at,
    }
    save_to_mongodb('reservations', {'id': instance.id}, rezervasyon_data)

@receiver(post_delete, sender=Rezervasyon)
def delete_rezervasyon_from_mongodb(sender, instance, **kwargs):
    delete_from_mongodb('reservations', {'id': instance.id})