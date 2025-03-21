from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.category_name}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank= True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254, blank= True)
    created_date = models.DateTimeField(default= timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to= 'picture/%Y/%m')
    category = models.ForeignKey(Category, on_delete= models.SET_NULL,
        blank= True, null= True)
    owner = models.ForeignKey( User, blank=True, null= True, 
        on_delete= models.SET_NULL)

    # Here we are defining the representation of the instance of class.
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'