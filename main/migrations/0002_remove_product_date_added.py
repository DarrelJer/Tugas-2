# Generated by Django 4.2.5 on 2023-09-19 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
    ]