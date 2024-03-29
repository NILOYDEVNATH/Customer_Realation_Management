# Generated by Django 2.2 on 2019-04-12 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190411_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('itemcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.CategoryModel')),
                ('itemsubcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.SubcategoryModel')),
            ],
        ),
    ]
