# Generated by Django 4.1.5 on 2023-01-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_anime_amount_of_episodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='image_url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='release_date',
            field=models.TextField(),
        ),
    ]