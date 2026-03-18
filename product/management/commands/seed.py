from django.core.management.base import BaseCommand
from django.core.management import call_command
from product.models import Category, Product
import requests
from decouple import config
import logging
from django.urls import reverse

logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = "Seed the database with product categories"

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write("Seeding items into DB ... 🚀⌛")
            # clear_table()
            populate_category()
            access_token = login_user()
            populate_products(access_token)
            self.stdout.write("Seeding completed ... 🎉✅")
        except Exception as e:
            self.stdout.write("An error occured while seeding into DB ... 🚀⌛")
            print(e)

def parse_url(url: str) -> str:
    return f'http://localhost:8000{url}'  

def clear_table():
    print("Clearing data from the Category table")
    logger.info("Clearing data from the Category table")
    Category.objects.all().delete()

def populate_category():
    # Implement array to keep track of all categories to be added to the database
    categories = [
        "Motors and vehicles parts",
        "Electronics",
        "Collectibles & Art",
        "Home & Garden", 
        "Clothing, Shoes & Accessories",
        "Toys & Hobbies",
        "Sporting Goods",
        "Books, Movies & Music",
        "Health & Beauty",
        "Business & Industrial",
        "Jewelry & Watches",
        "Baby Essentials",
        "Pet Supplies",
        "Tickets & Travel",
        "Gift Cards & Coupons",
        "Everything Else",
        "Real Estate",
        "Specialty Services"
    ]
    # Run loop to add all items to the database
    for cat in categories:
        category, created = Category.objects.get_or_create(name=cat)
        # category.save()
        logger.info("{} added to database", format(category))

# def populate_products():

def login_user():
    user_email = config("USER_EMAIL")
    user_password = config("USER_PASSWORD")
    response = requests.post("http://localhost:8000/api/v1/auth/login/", data={
        "email": user_email,
        "password": user_password
    })
    access = response.json().get("access", None)
    
    if access is None:
        print("Need to login user")
        return login_user()
    return access

def populate_products(access_token):
    products = [
    {
        "name": "Wireless Noise-Cancelling Headphones",
        "description": "Premium over-ear headphones with active noise cancellation, 30-hour battery life, and crystal-clear audio for an immersive listening experience.",
        "price": 129.99,
        "thumbnail": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
        "category": 76
    },
    {
        "name": "Leather Minimalist Wallet",
        "description": "Slim genuine leather bifold wallet with RFID blocking technology, fits up to 8 cards and cash without the bulk.",
        "price": 34.99,
        "thumbnail": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=400",
        "category": 79
    },
    {
        "name": "Stainless Steel Water Bottle",
        "description": "Double-walled vacuum insulated bottle that keeps drinks cold for 24 hours or hot for 12 hours. BPA-free and eco-friendly.",
        "price": 27.99,
        "thumbnail": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400",
        "category": 78
    },
    {
        "name": "Mechanical Keyboard",
        "description": "Compact TKL mechanical keyboard with tactile blue switches, RGB backlighting, and a durable aluminum frame for gamers and typists alike.",
        "price": 89.99,
        "thumbnail": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=400",
        "category": 76
    },
    {
        "name": "Scented Soy Candle Set",
        "description": "Set of 3 hand-poured soy wax candles in relaxing lavender, vanilla, and sandalwood scents. Each candle burns for up to 45 hours.",
        "price": 24.99,
        "thumbnail": "https://images.unsplash.com/photo-1608181831718-c9fbb4baf9ec?w=400",
        "category": 78
    },
    {
        "name": "Portable Bluetooth Speaker",
        "description": "Waterproof IPX7 portable speaker with 360-degree surround sound, 20-hour playtime, and a rugged design perfect for outdoor adventures.",
        "price": 59.99,
        "thumbnail": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400",
        "category": 76
    },
    {
        "name": "Ceramic Pour-Over Coffee Set",
        "description": "Handcrafted ceramic pour-over dripper with matching mug and a reusable stainless steel filter. The perfect gift for coffee enthusiasts.",
        "price": 44.99,
        "thumbnail": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400",
        "category": 78
    },
    {
        "name": "Yoga Mat Pro",
        "description": "Extra-thick 6mm non-slip yoga mat made from eco-friendly TPE material. Includes a carry strap and is sweat-resistant for intense sessions.",
        "price": 38.99,
        "thumbnail": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400",
        "category": 81
    },
    {
        "name": "Sunglasses Aviator Classic",
        "description": "Polarized UV400 aviator sunglasses with a lightweight metal frame, scratch-resistant lenses, and a timeless design for any face shape.",
        "price": 49.99,
        "thumbnail": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400",
        "category": 79
    },
    {
        "name": "Smart LED Desk Lamp",
        "description": "Touch-controlled desk lamp with 5 brightness levels, 3 color modes, USB charging port, and an auto-off timer. Great for studying or working from home.",
        "price": 32.99,
        "thumbnail": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400",
        "category": 78
    }
]
    for product in products:
        category = Category.objects.get(id=product['category'])
        products = Product(
            name=product['name'],
            description=product['description'],
            price=product['price'],
            thumbnail=product['thumbnail'],
            category=category
        )
        products.save()

    print("Products seeded successfully!!!")