# Generated by Django 4.2.7 on 2023-12-04 00:19

from django.db import migrations


def add_categorys(apps, schema_editor):
    Category = apps.get_model('base', 'Category')

    Category.objects.create(name='Салаты')
    Category.objects.create(name='Супы')
    Category.objects.create(name='Второе')
    Category.objects.create(name='Напитки')



class Migration(migrations.Migration):
    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [migrations.RunPython(add_categorys),]
