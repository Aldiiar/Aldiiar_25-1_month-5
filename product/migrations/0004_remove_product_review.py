# Generated by Django 4.1.7 on 2023-03-24 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_review_alter_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
    ]