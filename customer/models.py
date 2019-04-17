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

class CustomerdetailsModel(models.Model):
    company_name=models.CharField(max_length=255)
    phone=models.IntegerField()
    website=models.CharField(max_length=255)
    vat_number=models.CharField(max_length=255)
    address=models.TextField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    image=models.ImageField(upload_to="customer_details_image")

class groupModel(models.Model):
    customer_details=models.ForeignKey(CustomerdetailsModel,on_delete=models.CASCADE,default=1)
    group_data=models.CharField(max_length=255)


class BillingModel(models.Model):
    customer_details=models.ForeignKey(CustomerdetailsModel,on_delete=models.CASCADE,default=1)
    street_billing=models.CharField(max_length=255)
    city_billing=models.CharField(max_length=255)
    state_billing=models.CharField(max_length=255)
    zip_code_billing=models.CharField(max_length=255)
    country_billing=models.CharField(max_length=255)


