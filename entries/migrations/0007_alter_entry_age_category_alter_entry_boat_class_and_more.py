# Generated by Django 5.1.1 on 2024-10-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_alter_entry_age_category_alter_entry_boat_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='age_category',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='entry',
            name='boat_class',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='entry',
            name='sex_category',
            field=models.CharField(max_length=80),
        ),
    ]
