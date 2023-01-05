# Generated by Django 4.1.5 on 2023-01-05 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0003_anime_amount_of_episodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', models.BigIntegerField(default=0)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='animes.anime')),
            ],
        ),
    ]
