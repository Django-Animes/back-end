# Generated by Django 4.1.5 on 2023-01-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
