import json
from django.core.management.base import BaseCommand
from Rezervasyon.models import Rezervasyon
from Blog.models import BlogModel
from Reviews.models import Category, Food, Cart, Delivery, Order

class Command(BaseCommand):
    help = 'Export data to JSON file'

    def handle(self, *args, **kwargs):
        categories = list(Category.objects.all().values())
        foods = list(Food.objects.all().values())
        reservations = list(Rezervasyon.objects.all().values())
        blog_models = list(BlogModel.objects.all().values())
        cart = list(Cart.objects.all().values())
        delivery = list(Delivery.objects.all().values())
        order = list(Order.objects.all().values())

        data = {
            'categories': categories,
            'foods': foods,
            'reservations': reservations,
            'blog_models': blog_models,
            'cart': cart,
            'delivery': delivery,
            'order': order,
        }

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4, default=str)
