# Generated by Django 4.2.11 on 2024-03-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_remove_car_company_remove_car_reserved_car_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
