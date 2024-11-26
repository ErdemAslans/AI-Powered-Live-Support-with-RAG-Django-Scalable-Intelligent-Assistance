from django.db import models
from autoslug import AutoSlugField
from tinymce import models as tinymce_models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('title',)

class Category(BaseModel):
    def __str__(self):
        return self.title

class Food(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(upload_to='food_images/')
    description = tinymce_models.HTMLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    view_count = models.PositiveBigIntegerField(default=0)
    allergens = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f'{self.food.title} x {self.quantity}'
    
class Delivery(models.Model):
    STATUS_CHOICES = [
        ('preparing', 'Preparing'),  # Hazırlanıyor
        ('on_the_way', 'On the Way'),  # Yolda
        ('delivered', 'Delivered'),  # Teslim Edildi
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Siparişi veren kullanıcı
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparing')  # Sipariş durumu
    created_at = models.DateTimeField(auto_now_add=True)  # Siparişin oluşturulma zamanı
    updated_at = models.DateTimeField(auto_now=True)  # Siparişin güncellenme zamanı

    def __str__(self):
        return f"Delivery for {self.user} - {self.get_status_display()}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=100)
    date_ordered = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)  # Kullanıcıdan geri bildirim puanı
    allergies = models.TextField(blank=True, null=True)  # Alerjen bilgileri
    