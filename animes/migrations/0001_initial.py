# Generated by Django 4.1.5 on 2023-01-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image_url', models.TextField()),
                ('release_date', models.TextField()),
                ('description', models.TextField()),
                ('amount_of_episodes', models.IntegerField(default=0)),
                ('genres', models.ManyToManyField(related_name='animes', to='genres.genre')),
            ],
        ),
    ]
