# Generated by Django 4.1.5 on 2023-01-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animes", "0002_alter_anime_name"),
        ("profiles", "0004_rename_animes_viewed_episodes_viewed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="animes",
            field=models.ManyToManyField(related_name="profiles", to="animes.anime"),
        ),
    ]