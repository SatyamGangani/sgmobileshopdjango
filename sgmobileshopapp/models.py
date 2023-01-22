from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    slug = models.SlugField(null=True,unique=True)
    def __str__(self) :
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    image = models.ImageField(upload_to='brandlogo')
    
    def __str__(self) :
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
    mrp = models.FloatField()
    offer_price = models.FloatField()
    image = models.ImageField(upload_to='products_image')
    description = models.TextField(max_length=200)
    qty = models.IntegerField()
    def __str__(self) :
        return self.name