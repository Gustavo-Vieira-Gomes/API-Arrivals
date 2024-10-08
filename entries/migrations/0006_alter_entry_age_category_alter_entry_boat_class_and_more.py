# Generated by Django 5.1.1 on 2024-10-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_alter_entry_boat_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='age_category',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('+40', '+40'), ('SUB 20', 'SUB 20'), ('SENIOR', 'SENIOR'), ('MASTER A', 'MASTER A'), ('MASTER B', 'MASTER B')], max_length=80),
        ),
        migrations.AlterField(
            model_name='entry',
            name='boat_class',
            field=models.CharField(choices=[('OC6', 'OC6'), ('V6', 'V6'), ('OC2', 'OC2'), ('V2', 'V2'), ('OC1', 'OC1'), ('V1', 'V1'), ('TUR', 'Turismo'), ('OCI', 'Oceanico individual'), ('OCD', 'Oceanico duplo'), ('LFS', 'Lifesaving'), ('SFKI', 'Surfski individual'), ('SFKD', 'Surfski duplo'), ('PCD', 'Para-canoagem')], max_length=80),
        ),
        migrations.AlterField(
            model_name='entry',
            name='sex_category',
            field=models.CharField(choices=[('MALE', 'Masculino'), ('FEMALE', 'Feminino'), ('MIXED', 'Misto')], max_length=80),
        ),
    ]
