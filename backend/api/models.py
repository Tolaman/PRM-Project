from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# The Category model represents a product category in the e-commerce application. It has two fields: 
# name and slug. The name field is a character field with a maximum length of 100 characters and must 
# be unique. The slug field is a slug field that is also unique. The __str__ method returns the name of the category.
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True)

  def __str__(self):
    return self.name

# The Product model represents a product in the e-commerce application. It has a foreign key to the Category model,
class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='products/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

# The UserProfile model extends the built-in User model by adding additional fields for phone and address.
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(max_length=15, blank=True)
  address = models.TextField(blank=True)

  def __str__(self):
    return self.user.username

# The Order model represents a user's order. It has a foreign key to the User model, 
# a foreign key to the Product model, a quantity field, a total_amount field, and a 
# created_at field. The __str__ method returns a string representation of the order, which includes the order ID.
class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Order {self.id}"

# The OrderItem model represents an item in an order. It has a foreign key to the Order model, 
# a foreign key to the Product model, a quantity field, and a price field. The __str__ method 
# returns a string representation of the order item, which includes the quantity and product name.
class OrderItem(models.Model):
  order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"{self.quantity} x {self.product.name}"