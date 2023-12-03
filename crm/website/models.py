from django.db import models


# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Products(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=250)
    product_pictures = models.FileField()
    product_qte = models.IntegerField()
    product_date_build = models.CharField(max_length=20)
    product_date_expiration = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.product_name} : {self.product_price} FCFA"
