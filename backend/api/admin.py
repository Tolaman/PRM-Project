from django.contrib import admin
from .models import Category, Product, UserProfile, Order, OrderItem
# Register your models here.
# The following lines of code register the models defined in the `models.py` file with 
# the Django admin site. This allows you to manage these models through the Django admin interface.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
