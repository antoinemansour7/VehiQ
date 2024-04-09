# Generated by Django 4.2.10 on 2024-03-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("branches", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="branch",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="branch",
            name="opening_hours",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="branch",
            name="phone",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="branch",
            name="services",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
