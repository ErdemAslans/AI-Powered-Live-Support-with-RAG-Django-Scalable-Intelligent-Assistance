from pymongo import MongoClient
import json

# MongoDB bağlantı ayarları
client = MongoClient('mongodb+srv://Faymis123:Faymis1234@restorant.dmuoghs.mongodb.net/restaurant')
db = client.restaurant

# Koleksiyonlardan verileri çekmek
categories = list(db.Reviews_category.find())
foods = list(db.Reviews_food.find())
reservations = list(db.Rezervasyon_rezervasyon.find())
blog_models = list(db.Blog_blogmodel.find())
carts = list(db.Reviews_cart.find())
deliveries = list(db.Reviews_delivery.find())
orders = list(db.Reviews_order.find())

# Verileri JSON dosyasına kaydetmek
data = {
    'categories': categories,
    'foods': foods,
    'reservations': reservations,
    'blog_models': blog_models,
    'cart': carts,
    'delivery': deliveries,
    'order': orders,
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, default=str)

if 'categories' in data:
    db.Reviews_category.delete_many({})  # Mevcut verileri siler
    db.Reviews_category.insert_many(data['categories'])

# Yiyecekleri yükleme
if 'foods' in data:
    db.Reviews_food.delete_many({})
    db.Reviews_food.insert_many(data['foods'])

# Rezervasyonları yükleme
if 'reservations' in data:
    db.Rezervasyon_rezervasyon.delete_many({})
    db.Rezervasyon_rezervasyon.insert_many(data['reservations'])

# Blog modellerini yükleme
if 'blog_models' in data:
    db.Blog_blogmodel.delete_many({})
    db.Blog_blogmodel.insert_many(data['blog_models'])

# Sepetleri yükleme
if 'cart' in data:
    db.Reviews_cart.delete_many({})
    db.Reviews_cart.insert_many(data['cart'])

# Teslimatları yükleme
if 'delivery' in data:
    db.Reviews_delivery.delete_many({})
    db.Reviews_delivery.insert_many(data['delivery'])

# Siparişleri yükleme
if 'order' in data:
    db.Reviews_order.delete_many({})
    db.Reviews_order.insert_many(data['order'])

print("Veriler başarıyla yüklendi.")