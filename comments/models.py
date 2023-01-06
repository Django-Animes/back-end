from django.db import models


class Comment(models.Model):
    text = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.BigIntegerField(default=0)

    #profile = models.ForeignKey(
    #    "profile.Profile",
    #    on_delete=models.CASCADE,
    #    related_name="comments",
    #)
    
    episode = models.ForeignKey(
        "animes.Anime",
        on_delete=models.CASCADE,
        related_name="comments",
    )
