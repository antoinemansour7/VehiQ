# Generated by Django 4.2.11 on 2024-03-10 07:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField()),
                ('modification_allowed_until', models.DateTimeField()),
                ('reservation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vehicles.car')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
