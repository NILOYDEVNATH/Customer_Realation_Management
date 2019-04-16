from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=255)
    category_description = models.TextField()
    category_status = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class SubcategoryModel(models.Model):
    subcategory_name = models.CharField(max_length=255)
    category_name = models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING)
    sub_category_description=models.TextField()
    sub_category_status=models.CharField(max_length=30)

    def __str__(self):
        return self.subcategory_name

class ItemModel(models.Model):
    itemcategory_name = models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING)
    itemsubcategory_name = models.ForeignKey(SubcategoryModel,on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=255)
    item_image=models.ImageField(upload_to="images/")

class StatusModel(models.Model):
    quantity_on_hand=models.IntegerField()
    purchase_price=models.IntegerField()
    sales_price=models.IntegerField()
    
    