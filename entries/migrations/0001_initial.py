# Generated by Django 5.1.1 on 2024-09-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(blank=True, max_length=80, null=True)),
                ('name3', models.CharField(blank=True, max_length=80, null=True)),
                ('name4', models.CharField(blank=True, max_length=80, null=True)),
                ('name5', models.CharField(blank=True, max_length=80, null=True)),
                ('name6', models.CharField(blank=True, max_length=80, null=True)),
                ('boat_class', models.CharField(choices=[('OC6', 'OC6'), ('V6', 'V6'), ('OC2', 'OC2'), ('V2', 'V2'), ('OC1', 'OC1'), ('V1', 'V1'), ('TUR', 'Turismo'), ('OCI', 'Oceânico Individual'), ('OCD', 'Oceânico Duplo'), ('LFS', 'Lifesaving'), ('SFKI', 'Surfski Individual'), ('SFKD', 'Surfski Duplo'), ('PCD', 'Para-Canoagem')], max_length=10)),
                ('sex_category', models.CharField(choices=[('MALE', 'Masculino'), ('FEMALE', 'Feminino'), ('MIXED', 'Misto')], max_length=10)),
                ('age_category', models.CharField(choices=[('OPEN', 'OPEN'), ('+40', '+40'), ('SUB 20', 'SUB 20'), ('SENIOR', 'SENIOR'), ('MASTER A', 'MASTER A'), ('MASTER B', 'MASTER B')], max_length=15)),
                ('vest_number', models.IntegerField()),
            ],
        ),
    ]
