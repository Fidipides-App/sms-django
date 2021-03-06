# Generated by Django 3.2.5 on 2021-07-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('code', models.IntegerField(unique=True, verbose_name='Code')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('address', models.TextField(blank=True, max_length=255, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('postal_code', models.CharField(blank=True, max_length=8, verbose_name='Postal Code')),
                ('notes', models.TextField(blank=True, max_length=255, verbose_name='Notes')),
                ('birthdate', models.DateField(blank=True, verbose_name='Birth Date')),
            ],
            options={
                'verbose_name': 'Pacient',
                'verbose_name_plural': 'Pacients',
            },
        ),
    ]
