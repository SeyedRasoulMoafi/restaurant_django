# Generated by Django 4.1.3 on 2022-11-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_foods_delete_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='photo',
            field=models.ImageField(upload_to='foods_img/'),
        ),
    ]
