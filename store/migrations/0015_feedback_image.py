# Generated by Django 3.1.7 on 2021-04-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210412_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='feedback'),
        ),
    ]