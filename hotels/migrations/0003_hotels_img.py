# Generated by Django 3.0.6 on 2020-06-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_hotels_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
    ]
