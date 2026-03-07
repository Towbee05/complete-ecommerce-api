from django.core.management.base import BaseCommand
from django.core.management import call_command
from product.models import Category
import logging

logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = "Seed the database with product categories"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding category into DB ... 🚀⌛")
        populate_category()
        self.stdout.write("Seeding completed ... 🎉✅")


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
        category = Category(name=cat)
        category.save()
        logger.info("{} added to database", format(category))