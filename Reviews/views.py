from django.shortcuts import render, get_object_or_404
from .models import Category, Food, Cart, CartItem, Delivery, Order
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from .models import Category, Food, Cart, CartItem, Delivery, Order
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    foods = Food.objects.filter(category=category, is_active=True)
    context = {'category': category, 'foods': foods}
    return render(request, 'category_detail.html', context)

def food_detail(request, category_slug, food_slug):
    category = get_object_or_404(Category, slug=category_slug)
    food = get_object_or_404(Food, slug=food_slug, category=category)
    return render(request, 'food_detail.html', {'category': category, 'food': food})

@login_required
def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, food=food)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('reviews:cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('reviews:cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.food.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        allergies = request.POST.get('allergies', '')
        if cart_items.exists():
            for item in cart_items:
                Order.objects.create(user=request.user, food_item=item.food.title, rating=0, allergies=allergies)
            cart_items.delete()  # Sepeti boşalt
        return redirect('reviews:delivery_status')

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart_detail.html', context)

@login_required
def delivery_status(request):
    deliveries = Delivery.objects.filter(user=request.user)

    # Teslimat tamamlanmışsa veritabanından sil
    completed_deliveries = deliveries.filter(status='delivered')
    if completed_deliveries.exists():
        completed_deliveries.delete()

    context = {'deliveries': deliveries}
    return render(request, 'delivery_status.html', context)

@login_required
def delivery(request):
    # POST isteği ile gelirse aktif bir teslimat oluştur
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        if cart_items.exists():
            Delivery.objects.create(user=request.user)
            cart_items.delete()  # Sepeti boşalt
        return redirect('reviews:delivery_status')