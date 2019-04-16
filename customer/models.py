from django.db import models

# Create your models here.

class CustomeragetModel(models.Model):
    title=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    company_name=models.CharField(max_length=255)
    sales_team=models.CharField(max_length=255)
    Email=models.EmailField()
    phone=models.IntegerField()
    mobile=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    sendemail=models.EmailField()