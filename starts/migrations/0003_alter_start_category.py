# Generated by Django 5.1.1 on 2024-10-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starts', '0002_alter_start_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start',
            name='category',
            field=models.CharField(choices=[('OC6', ''), ('V6', ''), ('OC2', ''), ('V2', ''), ('OC1', ''), ('V1', ''), ('Turismo', ''), ('Oceanico individual', ''), ('Oceanico duplo', ''), ('Lifesaving', ''), ('Surfski individual', ''), ('Surfski duplo', ''), ('Para-canoagem', '')], max_length=80),
        ),
    ]
