from rest_framework import serializers
from django.db import models
from .models import Anime
from genres.models import Genre
from episodes.models import Episode
from genres.serializer import GenreSerializer
from episodes.serializer import AnimeEpisodeSerializer
import ipdb

class AnimeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Anime
        fields = "__all__"
    genres = GenreSerializer(many=True,required=True)
    episodes = AnimeEpisodeSerializer(many=True,required=False)
    amount_of_episodes = serializers.SerializerMethodField()

    def get_amount_of_episodes(self,obj):
        return len(obj.episodes.all())
        
    def create(self, validated_data: dict):
        genres: list = validated_data.pop("genres")
        newGenres = []
        for genre in genres:
            genre = genre['name']
            genre,_ = Genre.objects.get_or_create(name=genre) 
            newGenres.append(genre)
        anime,_ = Anime.objects.get_or_create(**validated_data)
        anime.genres.set(newGenres)
        return anime
    def update(self, instance : dict, validated_data: dict):
        episodes = validated_data.pop("episodes",None)
        genres = validated_data.pop("genres",None)
        for key,value in validated_data.items():
            setattr(instance,key,value)
        return instance       