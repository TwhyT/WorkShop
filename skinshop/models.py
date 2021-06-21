from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='upload/', null=True, blank=False)
    detail = models.TextField(max_length=255)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    published = models.BooleanField(default=False)
    detail = models.TextField(max_length=255)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, null=True, blank=True, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    recommend = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='upload/', null=True, blank=False)
    detail = models.TextField(max_length=255)

    class Meta:
        ordering = ['name','price']

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='upload/', null=True, blank=True) 

class Contact(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    Email = models.EmailField(max_length=50, blank=False)
    detail = models.TextField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Email