# Generated by Django 5.2 on 2025-04-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CargoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Cargo Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('weight', models.FloatField(verbose_name='Weight (kg)')),
                ('volume', models.FloatField(verbose_name='Volume (m³)')),
                ('value', models.FloatField(verbose_name='Value ($)')),
                ('destination', models.CharField(max_length=255, verbose_name='Destination')),
                ('delivery_date', models.DateField(verbose_name='Delivery Date')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'ordering': ['delivery_date'],
            },
        ),
    ]
