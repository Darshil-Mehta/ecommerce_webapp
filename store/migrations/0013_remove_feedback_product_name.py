# Generated by Django 3.1.7 on 2021-04-12 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210412_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='product_name',
        ),
    ]