# Generated by Django 2.2 on 2019-04-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190413_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='item_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
