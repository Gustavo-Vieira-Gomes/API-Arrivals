# Generated by Django 5.1.1 on 2024-10-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starts', '0004_alter_start_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start',
            name='category',
            field=models.CharField(choices=[('OC6', ''), ('GERAL', '')], max_length=6, unique=True),
        ),
    ]
