# Generated by Django 5.1.1 on 2024-09-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrivals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrival',
            name='arrival_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
