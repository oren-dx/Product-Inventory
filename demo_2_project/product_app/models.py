from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    full_name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f'{self.username}'
    

class ProductDataModel(models.Model):
    STATUS_CHOICES =[
        ('Available','Available'),
        ('Out of Stocle','Out of Stock'),
    ]
     
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    qty = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='media/products_img',null=True)
    status = models.CharField(choices=STATUS_CHOICES ,max_length=20,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
    
    
     
